"""
MJKMH yayın listesini Scopus'tan günceller.

Ne yapar
  1. scripts/scopus_ayarlar.yml'deki her üyenin Scopus yayınlarını pybliometrics ile çeker
     (Scopus.ipynb notebook'undaki adımların aynısı).
  2. Ortak yayınları tekilleştirir, eksik yazar listelerini/özetleri AbstractRetrieval ile tamamlar,
     dergi CiteScore yüzdeliğinden Q etiketini hesaplar.
  3. Mevcut _data/yayinlar.yml ile birleştirir: elle girilmiş alanlar (year, date, title, image,
     image_credit, abstract) ve "manuel: true" işaretli kayıtlar korunur.
  4. Yazar:
       _data/yayinlar.yml              -> GitHub sitesi (mjkmh.github.io)
       sitefinity/yayinlar.html  -> mjkmh.itu.edu.tr Yayınlar sayfasına yapıştırılacak blok

Kullanım (depo klasöründe, API anahtarının tanımlı olduğu bilgisayarda)
  python scripts/scopus_guncelle.py                 # Scopus API'den çek
  python scripts/scopus_guncelle.py --crossref      # yeni yayınların tarihlerini Crossref'ten de al
  python scripts/scopus_guncelle.py --excel DOSYA   # API yerine notebook'un Excel dışa aktarımını kullan

Gerekenler: pip install pybliometrics pandas pyyaml openpyxl
API anahtarı pybliometrics'in kendi ayar dosyasında durur (pybliometrics.init()); bu depoya yazılmaz.
"""

import argparse
import html
import json
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

import yaml

KOK = Path(__file__).resolve().parent.parent
AYAR = KOK / "scripts" / "scopus_ayarlar.yml"
YAYIN_YML = KOK / "_data" / "yayinlar.yml"
CONFIG = KOK / "_config.yml"
CIKTI = KOK / "sitefinity"

KORUNAN_ALANLAR = ["year", "date", "title", "authors", "image", "image_credit", "abstract"]


# ---------------------------------------------------------------- yardımcılar
def bos(v):
    if v is None:
        return True
    try:
        import math
        if isinstance(v, float) and math.isnan(v):
            return True
    except Exception:
        pass
    return str(v).strip() in ("", "nan", "None")


def metin(v):
    return None if bos(v) else str(v).strip()


def norm_baslik(s):
    return re.sub(r"\W+", "", str(s or "").lower())


def norm_doi(s):
    return (metin(s) or "").lower()


def ayir(v, sep=";"):
    if bos(v):
        return []
    return [x.strip() for x in str(v).split(sep) if x.strip()]


def indeks_ad(ad):
    """'Zengin, Enes' -> 'Zengin E.'"""
    if "," not in ad:
        return ad.strip()
    soyad, isim = [x.strip() for x in ad.split(",", 1)]
    bas = "".join(p[0] + "." for p in isim.replace("-", " ").split() if p)
    return f"{soyad} {bas}".strip()


def ceyrek(yuzdelik):
    if yuzdelik is None:
        return None
    y = float(yuzdelik)
    return "(Q1 - Scopus)" if y >= 75 else "(Q2 - Scopus)" if y >= 50 else "(Q3 - Scopus)" if y >= 25 else "(Q4 - Scopus)"


def temiz_issn(v):
    v = metin(v)
    if not v:
        return None
    v = v.replace("-", "").replace(",", " ").replace(";", " ").split()
    return v[0] if v else None


def scopus_ara(sid, anahtar, token=None):
    """Scopus Search API ile bir yazarın yayınlarını çeker (kurum dışı erişimde 25'erli sayfalar)."""
    from types import SimpleNamespace
    if not anahtar:
        import pybliometrics.utils as pu
        anahtar = pu.config["Authentication"]["APIKey"].split(",")[0].strip()
    bas, sonuc = 0, []
    while True:
        url = ("https://api.elsevier.com/content/search/scopus?view=STANDARD&count=25"
               f"&start={bas}&query=AU-ID({sid})")
        bas_lik = {"X-ELS-APIKey": anahtar, "Accept": "application/json"}
        if token:
            bas_lik["X-ELS-Insttoken"] = token
        veri = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=bas_lik), timeout=30))
        sr = veri["search-results"]
        girdiler = [e for e in sr.get("entry") or [] if "error" not in e]
        for e in girdiler:
            sonuc.append(SimpleNamespace(
                eid=e.get("eid"), doi=e.get("prism:doi"), title=e.get("dc:title"),
                coverDate=e.get("prism:coverDate"), subtypeDescription=e.get("subtypeDescription"),
                publicationName=e.get("prism:publicationName"),
                issn=e.get("prism:issn") or e.get("prism:eIssn"),
                volume=e.get("prism:volume"), issueIdentifier=e.get("prism:issueIdentifier"),
                pageRange=e.get("prism:pageRange"), article_number=e.get("article-number"),
                author_names=None, author_ids=None, description=None))
        bas += 25
        if not girdiler or bas >= int(sr.get("opensearch:totalResults", 0)):
            return sonuc
        time.sleep(0.3)


def crossref_yazarlar(k):
    """Yazar listesi Scopus'tan alınamazsa DOI üzerinden Crossref'ten alır (yazar ID'si olmadan)."""
    if not k.get("doi"):
        return
    try:
        req = urllib.request.Request(f"https://api.crossref.org/works/{k['doi']}",
                                     headers={"User-Agent": "mjkmh-yayin-guncelleme"})
        msg = json.load(urllib.request.urlopen(req, timeout=20))["message"]
        adlar = []
        for a in msg.get("author") or []:
            if a.get("family"):
                adlar.append(indeks_ad(f"{a['family']}, {a.get('given', '')}"))
        if adlar:
            k["yazar_adlari"], k["yazar_idleri"] = adlar, []
        if bos(k.get("ozet")) and msg.get("abstract"):
            k["ozet"] = re.sub(r"<[^>]+>", "", msg["abstract"]).strip()
    except Exception as e:
        print(f"  yazar listesi tamamlanamadı {k.get('doi')}: {e}")


# ---------------------------------------------------------------- Scopus API
def api_ile_topla(uyeler):
    import os
    import pybliometrics
    from pybliometrics.scopus import AbstractRetrieval, AuthorRetrieval, SerialTitleISSN

    # GitHub Actions'ta anahtar ortam değişkeninden gelir; kendi bilgisayarınızda ayar dosyasından okunur.
    anahtar = os.environ.get("SCOPUS_API_KEY")
    token = os.environ.get("SCOPUS_INSTTOKEN")
    if anahtar:
        pybliometrics.init(keys=[anahtar], inst_tokens=[token] if token else None)
    else:
        pybliometrics.init()
    kayitlar, hatalar = [], []
    for u in uyeler:
        sid = str(u["scopus_id"])
        try:
            try:
                au = AuthorRetrieval(sid, refresh=True, view="ENHANCED")
                try:
                    docs = au.get_documents(refresh=True, view="COMPLETE")
                except Exception:
                    docs = au.get_documents(refresh=True)
                yol = "yazar profili"
            except Exception:
                # Kurum ağı dışında (ör. GitHub) yazar profili kapalıdır; Scopus Search açıktır.
                docs = scopus_ara(sid, anahtar, token)
                yol = "Scopus Search"
            print(f"  {u['ad']:<16} {len(docs)} yayın ({yol})")
            for d in docs:
                kayitlar.append({
                    "eid": getattr(d, "eid", None),
                    "doi": getattr(d, "doi", None),
                    "title": getattr(d, "title", None),
                    "cover_date": str(getattr(d, "coverDate", "") or ""),
                    "tur_en": getattr(d, "subtypeDescription", None),
                    "source": getattr(d, "publicationName", None),
                    "issn": getattr(d, "issn", None),
                    "volume": getattr(d, "volume", None),
                    "issue": getattr(d, "issueIdentifier", None),
                    "pages": getattr(d, "pageRange", None),
                    "article_no": getattr(d, "article_number", None),
                    "yazar_adlari": [indeks_ad(n) for n in ayir(getattr(d, "author_names", None))],
                    "yazar_idleri": ayir(getattr(d, "author_ids", None)),
                    "ozet": getattr(d, "description", None),
                    "uye_id": sid,
                })
            time.sleep(0.5)
        except Exception as e:
            print(f"  HATA {u['ad']} ({sid}): {e}")
            hatalar.append(u["ad"])

    if hatalar:
        sys.exit("Şu üyelerin yayınları alınamadı: " + ", ".join(hatalar)
                 + ". Eksik liste yazılmasın diye dosyalar değiştirilmedi.")
    tekil = tekillestir(kayitlar)

    # Yazar listesi eksik kalanları tek tek tamamla
    for k in tekil:
        if k["yazar_idleri"] and k["yazar_adlari"]:
            continue
        if not k["eid"]:
            continue
        try:
            ab = AbstractRetrieval(k["eid"], view="META_ABS", refresh=30)
            if ab.authors:
                k["yazar_adlari"] = [a.indexed_name for a in ab.authors]
                k["yazar_idleri"] = [str(a.auid) for a in ab.authors]
            if bos(k["ozet"]):
                k["ozet"] = ab.abstract or ab.description
        except Exception:
            crossref_yazarlar(k)
        time.sleep(0.3)

    # Dergi CiteScore yüzdelikleri
    onbellek = {}
    for k in tekil:
        issn = temiz_issn(k["issn"])
        if not issn:
            continue
        if issn not in onbellek:
            onbellek[issn] = None
            try:
                src = SerialTitleISSN(issn, view="CITESCORE", refresh=30)
                bilgi = src.citescoreyearinfolist or []
                if bilgi:
                    al = lambda o, a: o.get(a) if isinstance(o, dict) else getattr(o, a, None)
                    son = sorted(bilgi, key=lambda x: int(al(x, "year")), reverse=True)[0]
                    yuzde = []
                    for r in al(son, "rank") or []:
                        p = r.get("percentile") if isinstance(r, dict) else getattr(r, "percentile", None)
                        if p is None and isinstance(r, (list, tuple)) and len(r) >= 3:
                            p = r[2]
                        if p is not None:
                            yuzde.append(float(p))
                    onbellek[issn] = max(yuzde) if yuzde else None
            except Exception:
                pass
            time.sleep(0.5)
        k["yuzdelik"] = onbellek[issn]
    return tekil


# ---------------------------------------------------------------- Excel (notebook dışa aktarımı)
def excel_ile_topla(dosya):
    import pandas as pd

    t = pd.read_excel(dosya, sheet_name="Tekil Yayinlar")
    kayitlar = []
    for _, r in t.iterrows():
        kayitlar.append({
            "eid": metin(r.get("EID")),
            "doi": metin(r.get("DOI")),
            "title": metin(r.get("Başlık")),
            "cover_date": str(r.get("Yıl") or ""),
            "tur_en": metin(r.get("Yayın Türü")),
            "source": metin(r.get("Kaynak Adı")),
            "issn": metin(r.get("ISSN")),
            "volume": None, "issue": None, "pages": None, "article_no": None,
            "yazar_adlari": ayir(r.get("Yazarlar"), ","),
            "yazar_idleri": ayir(r.get("Yazar Scopus ID'leri"), ","),
            "ozet": metin(r.get("Özet")),
            "yuzdelik": None if bos(r.get("Highest Percentile")) else float(r.get("Highest Percentile")),
        })
    return tekillestir(kayitlar)


# ---------------------------------------------------------------- birleştirme
def tekillestir(kayitlar):
    """Önce EID ile, sonra başlıkla tekilleştirir; DOI'li ve daha dolu kaydı tutar."""
    gorulen, sonuc = {}, []
    for k in kayitlar:
        anahtar = k.get("eid") or norm_doi(k.get("doi")) or norm_baslik(k.get("title"))
        if anahtar in gorulen:
            if k.get("uye_id"):
                gorulen[anahtar].setdefault("uye_idleri", set()).add(k["uye_id"])
            continue
        k["uye_idleri"] = {k["uye_id"]} if k.get("uye_id") else set()
        gorulen[anahtar] = k
        sonuc.append(k)
    basliga_gore = {}
    for k in sonuc:
        b = norm_baslik(k["title"])
        onceki = basliga_gore.get(b)
        if onceki is None:
            basliga_gore[b] = k
            continue
        puan = lambda x: (bool(x.get("doi")), len(x.get("yazar_idleri") or []), bool(x.get("ozet")))
        if puan(k) > puan(onceki):
            basliga_gore[b] = k
    return list(basliga_gore.values())


def sade(s):
    tablo = str.maketrans("çğıöşüÇĞİÖŞÜâîû", "cgiosuCGIOSUaiu")
    return re.sub(r"[^a-z]", "", str(s).translate(tablo).lower())


def soyad_esit(uye, ad):
    """'Zengin E.' ile 'Zengin E.' / 'Ündül Ö.' ile 'Undul O.' gibi yazımları eşleştirir."""
    u_soyad, _, u_bas = uye.rpartition(" ")
    a_soyad, _, a_bas = ad.rpartition(" ")
    return sade(u_soyad) == sade(a_soyad) and sade(u_bas)[:1] == sade(a_bas)[:1]


def kaynak_ayrinti(k):
    parca = []
    if k.get("volume"):
        parca.append(str(k["volume"]) + (f"({k['issue']})" if k.get("issue") else ""))
    if k.get("pages"):
        parca.append(str(k["pages"]))
    elif k.get("article_no"):
        parca.append(str(k["article_no"]))
    return ", ".join(parca) or None


def girdileri_kur(tekil, ayar, mevcut, detayli_yillar):
    uye_ad = {str(u["scopus_id"]): u["ad"] for u in ayar["uyeler"]}
    haric_tur = set(ayar.get("haric_turler") or [])
    haric = {str(x).lower() for x in (ayar.get("haric_yayinlar") or [])}
    tur_tr = ayar.get("tur_adlari") or {}

    doi_ile = {norm_doi(e.get("doi")): e for e in mevcut if e.get("doi")}
    baslik_ile = {norm_baslik(e.get("title")): e for e in mevcut}

    girdiler, eslesen = [], set()
    for k in tekil:
        if k.get("tur_en") in haric_tur:
            continue
        if (k.get("eid") or "").lower() in haric or norm_doi(k.get("doi")) in haric:
            continue
        yazarlar = []
        idler = k.get("yazar_idleri") or []
        uye_idleri = set(k.get("uye_idleri") or [])
        for i, ad in enumerate(k.get("yazar_adlari") or []):
            aid = idler[i] if i < len(idler) else None
            if aid and aid in uye_ad:
                yazarlar.append({"n": uye_ad[aid], "m": True})
                continue
            if not idler:  # ID yoksa (Crossref) soyadı + baş harfle eşleştir
                eslesme = [u for u in uye_idleri if soyad_esit(uye_ad[u], ad)]
                if eslesme:
                    yazarlar.append({"n": uye_ad[eslesme[0]], "m": True})
                    continue
            yazarlar.append({"n": ad})
        g = {
            "year": int(str(k["cover_date"])[:4]) if str(k.get("cover_date"))[:4].isdigit() else None,
            "date": k["cover_date"] if len(str(k.get("cover_date"))) == 10 else None,
            "title": metin(k["title"]),
            "authors": yazarlar,
            "source": metin(k["source"]),
            "source_detail": kaynak_ayrinti(k),
            "type": tur_tr.get(k.get("tur_en"), k.get("tur_en")),
            "quartile": ceyrek(k.get("yuzdelik")),
            "top_percent": None if k.get("yuzdelik") is None else max(1, round(100 - float(k["yuzdelik"]))),
            "doi": metin(k.get("doi")),
            "eid": metin(k.get("eid")),
            "abstract": metin(k.get("ozet")),
        }
        eski = doi_ile.get(norm_doi(g["doi"])) if g["doi"] else None
        eski = eski or baslik_ile.get(norm_baslik(g["title"]))
        if eski is not None and not any(eski is m for m in mevcut):
            eski = None
        g["_sira"] = mevcut.index(eski) if eski in mevcut else len(mevcut)
        if eski:
            eslesen.add(id(eski))
            for alan in KORUNAN_ALANLAR:
                if eski.get(alan) not in (None, ""):
                    g[alan] = eski[alan]
                elif alan == "abstract":
                    g[alan] = None if str(g["year"]) not in detayli_yillar else g[alan]
        elif str(g["year"]) not in detayli_yillar:
            g["abstract"] = None
        girdiler.append(g)

    # Elle eklenmiş ("manuel: true") kayıtları koru
    for e in mevcut:
        if e.get("manuel") and id(e) not in eslesen:
            e = dict(e); e["_sira"] = mevcut.index(e) if e in mevcut else 0
            girdiler.append(e)

    girdiler.sort(key=lambda g: g.get("_sira", 0))
    girdiler.sort(key=lambda g: (int(g.get("year") or 0), str(g.get("date") or "")), reverse=True)
    for g in girdiler:
        g.pop("_sira", None)
    return girdiler


# ---------------------------------------------------------------- yazıcılar
def q(s):
    return json.dumps(str(s), ensure_ascii=False)


def yml_yaz(girdiler, kaynak):
    sat = [
        f"# Yayınlar — scripts/scopus_guncelle.py ile üretildi ({kaynak}, {date.today():%d.%m.%Y}).",
        "# Elle düzeltilen alanlar (year, date, title, image, image_credit, abstract) sonraki güncellemelerde korunur.",
        "# Elle eklenen ve Scopus'ta olmayan bir kayıt silinmesin isteniyorsa ona 'manuel: true' ekleyin.",
        "# authors: tüm yazarlar; m: true = MJKMH üyesi (sitede koyu kırmızı)",
        "# quartile: Scopus CiteScore çeyreği; top_percent: alanındaki en iyi yüzdelik dilim (İlk %X)",
        "# abstract, image, image_credit: _config.yml yayin_detayli_yillar içindeki yıllarda gösterilir",
        "#   (image: images/yayinlar/ içindeki dosya; yoksa gri kare)",
        "",
    ]
    sira = ["year", "date", "title", "authors", "source", "source_detail", "type", "quartile",
            "top_percent", "doi", "eid", "manuel", "abstract", "image", "image_credit"]
    for g in girdiler:
        ilk = True
        for alan in sira + [a for a in g if a not in sira]:
            v = g.get(alan)
            if v in (None, "", []):
                continue
            on = "- " if ilk else "  "
            ilk = False
            if alan == "authors":
                sat.append(f"{on}authors:")
                for a in v:
                    sat.append(f"    - {{n: {q(a['n'])}" + (", m: true}" if a.get("m") else "}"))
            elif alan in ("year", "top_percent") or isinstance(v, bool):
                sat.append(f"{on}{alan}: {str(v).lower() if isinstance(v, bool) else v}")
            elif alan == "type":
                sat.append(f"{on}{alan}: {v}")
            else:
                sat.append(f"{on}{alan}: {q(v)}")
        sat.append("")
    YAYIN_YML.write_text("\n".join(sat), encoding="utf-8")


def html_yaz(girdiler):
    e = html.escape
    yillar = {}
    for g in girdiler:
        yillar.setdefault(g.get("year"), []).append(g)
    p = ['<div class="mjkmh-pubs">', "",
         f'<p class="note">Kaynak: Scopus · Toplam {len(girdiler)} yayın · Son güncelleme: {date.today():%d.%m.%Y}</p>']
    for yil in sorted(yillar, key=lambda x: x or 0, reverse=True):
        liste = yillar[yil]
        p.append(f'<h3>{yil} <span class="count">({len(liste)})</span></h3>')
        p.append("<ol>")
        for g in liste:
            yz = ", ".join(f"<strong>{e(a['n'])}</strong>" if a.get("m") else e(a["n"]) for a in g.get("authors") or [])
            kaynak = e(g.get("source") or "") + (f", {e(g['source_detail'])}" if g.get("source_detail") else "")
            s = f"    <li>{yz} ({g.get('year')}). {e(g.get('title') or '')}. <em>{kaynak}</em>."
            if g.get("doi"):
                s += f' <a href="https://doi.org/{e(g["doi"])}" target="_blank" rel="noopener">doi:{e(g["doi"])}</a>'
            if g.get("type"):
                s += f' <span class="tag">{e(g["type"])}</span>'
            if g.get("top_percent"):
                s += f' <span class="tag">İlk %{g["top_percent"]}</span>'
            p.append(s + "</li>")
        p.append("</ol>")
    p.append("</div>")
    CIKTI.mkdir(exist_ok=True)
    yol = CIKTI / "yayinlar.html"
    yol.write_text("\n".join(p), encoding="utf-8")
    return yol


def crossref_tarihleri(girdiler):
    """Tarihi olmayan, DOI'li kayıtların yayın tarihini Crossref'ten alır."""
    for g in girdiler:
        if g.get("date") or not g.get("doi"):
            continue
        try:
            req = urllib.request.Request(f"https://api.crossref.org/works/{g['doi']}",
                                         headers={"User-Agent": "mjkmh-yayin-guncelleme"})
            msg = json.load(urllib.request.urlopen(req, timeout=20))["message"]
            for alan in ("published-online", "published-print", "issued"):
                dp = (msg.get(alan) or {}).get("date-parts")
                if dp and len(dp[0]) == 3:
                    g["date"] = "%04d-%02d-%02d" % tuple(dp[0])
                    break
        except Exception:
            pass
        time.sleep(0.2)


# ---------------------------------------------------------------- ana akış
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--excel", help="API yerine Scopus.ipynb'nin Excel dışa aktarımını kullan")
    ap.add_argument("--crossref", action="store_true", help="Eksik yayın tarihlerini Crossref'ten tamamla")
    a = ap.parse_args()

    ayar = yaml.safe_load(AYAR.read_text(encoding="utf-8"))
    mevcut = yaml.safe_load(YAYIN_YML.read_text(encoding="utf-8")) if YAYIN_YML.exists() else []
    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}
    detayli = {str(x) for x in cfg.get("yayin_detayli_yillar") or []}

    if a.excel:
        print("Excel'den okunuyor:", a.excel)
        tekil, kaynak = excel_ile_topla(a.excel), Path(a.excel).name
    else:
        print("Scopus API'den çekiliyor...")
        tekil, kaynak = api_ile_topla(ayar["uyeler"]), "Scopus API"
    if not tekil:
        sys.exit("Hiç yayın gelmedi; API anahtarını ve bağlantıyı kontrol edin. Dosyalar değiştirilmedi.")

    girdiler = girdileri_kur(tekil, ayar, mevcut or [], detayli)
    if mevcut and len(girdiler) < 0.9 * len(mevcut):
        sys.exit(f"Gelen liste ({len(girdiler)}) mevcut listeden ({len(mevcut)}) belirgin biçimde kısa; "
                 "erişim kısıtlı olabilir. Dosyalar değiştirilmedi.")
    if a.crossref:
        crossref_tarihleri(girdiler)
        girdiler.sort(key=lambda g: (int(g.get("year") or 0), str(g.get("date") or "")), reverse=True)

    eski = {norm_doi(e.get("doi")) or norm_baslik(e.get("title")) for e in (mevcut or [])}
    yeni = [g for g in girdiler if (norm_doi(g.get("doi")) or norm_baslik(g.get("title"))) not in eski]

    yml_yaz(girdiler, kaynak)
    yol = html_yaz(girdiler)
    print(f"\nToplam {len(girdiler)} yayın ({len(yeni)} yeni).")
    for g in yeni:
        print(f"  + {g.get('year')}  {g.get('title')}")
    print(f"\nYazıldı: {YAYIN_YML.relative_to(KOK)}")
    print(f"Yazıldı: {yol.relative_to(KOK)}  (mjkmh.itu.edu.tr Yayınlar sayfası için)")
    print("\nSonraki adım:  git add _data/yayinlar.yml sitefinity && git commit -m \"Yayınlar güncellendi\" && git push")


if __name__ == "__main__":
    main()
