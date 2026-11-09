"""Araştırmacı CV sayfalarının içerik bloklarını üretir: sitefinity/cv-<slug>.html
Kaynak: _data/cv.yml (kişisel bilgiler), _data/yayinlar.yml (Scopus), _data/projeler.yml."""
import html, re, sys
from pathlib import Path
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parent))
from scopus_guncelle import istatistik, etiket, TUR_RENK, Q_RENK, UYE  # noqa: E402

KOK = Path(__file__).resolve().parent.parent
e = html.escape
LAC = "#062a54"
# Etiket renk sistemi (tüm CV sayfaları): renk yalnızca anlam taşıyan yerde
# Q: yeşil→kırmızı (scopus_guncelle.Q_RENK) · Yürütücü: koyu lacivert · diğer görevler: açık lacivert
# Devam Ediyor: açık mavi · Tam metin/Özet/Sözlü/Poster ve indeksler: her biri ayrı açık renk, çerçevesiz
ROL_RENK = {"Yürütücü": ("#062a54", "#ffffff")}
DIGER_ROL = ("#e8eef8", "#062a54")
DEVAM = ("#e3f0fb", "#1f5fa8")
GRI = ("#f0f0f0", "#666666")
FORMAT_RENK = {"Tam metin": ("#dff3f1", "#00695c"), "Özet": ("#eeeeee", "#555555"),
               "Sözlü": ("#f1e6fa", "#6a3d9a"), "Poster": ("#fce4ef", "#a2185b")}
IND_RENK = {"TR Dizin": ("#efe6da", "#6d4c2f"), "DOAJ": ("#dff1f7", "#0b6e85"),
            "ESCI": ("#e9eaf7", "#3c3f8f"), "SCI-E": ("#e6efe3", "#3d5f2e")}


def cerceve(metin_):
    return (f'<span class="tag" style="display:inline-block;font-size:12px;line-height:1.6;padding:0 8px;margin-left:4px;'
            f'border-radius:10px;white-space:nowrap;background:#ffffff;color:#062a54;border:1px solid #062a54;">{e(metin_)}</span>')
LOGO = "/images/librariesprovider187/mjkmh-kisiler/logo-{}.png"
LOGO_AD = {"ORCID": "orcid", "Scopus": "scopus", "Google Scholar": "scholar", "ResearchGate": "researchgate", "LinkedIn": "linkedin"}


def baslik(t, n=None):
    say = f' <span style="color:#999;font-weight:normal;font-size:15px;">({n})</span>' if n is not None else ""
    return (f'<h3 style="margin:34px 0 14px 0;padding-bottom:8px;border-bottom:2px solid #e3e8ef;color:{LAC};">'
            f'{e(t)}{say}</h3>')


def ust(k, logolar):
    ikon = "".join(f'<a href="{e(u)}" target="_blank" title="{e(ad)}" style="display:inline-block;margin:0 6px 0 0;">'
                   f'<img src="{logolar.get(ad, "")}" alt="{e(ad)}" width="24" height="24" style="width:24px;height:24px;" /></a>'
                   for ad, u in (k.get("profiller") or {}).items())
    return (f'<div>'
            f'<div style="display:inline-block;vertical-align:top;margin:0 24px 14px 0;">'
            f'<img src="{e(k["foto"])}" alt="{e(k["ad"])}" width="160" height="160" style="width:160px;height:160px;display:block;" /></div>'
            f'<div style="display:inline-block;vertical-align:top;width:calc(100% - 190px);min-width:260px;">'
            f'<p style="margin:0;font-size:14px;color:#777;">{e(k["unvan"])}</p>'
            f'<p style="margin:0 0 8px 0;font-size:28px;font-weight:bold;color:{LAC};line-height:1.2;">{e(k["ad"])}</p>'
            f'<p style="margin:0 0 4px 0;font-size:14px;color:#555;">İTÜ Maden Fakültesi, Jeoloji Mühendisliği Bölümü</p>'
            f'<p style="margin:0 0 12px 0;font-size:14px;"><a href="mailto:{e(k["eposta"])}">{e(k["eposta"])}</a></p>'
            f'<p style="margin:0;">{ikon}</p></div></div>')


def kutular(say):
    k = [(say["makale"], "Makale"), (say["ilk10"], "İlk %10’luk Dilimdeki Makale"), (say["Q1"], "Q1 Makale")]
    return '<div style="margin:22px 0 0 0;">' + "".join(
        f'<div style="display:inline-block;vertical-align:top;min-width:150px;margin:0 12px 10px 0;padding:12px 16px;'
        f'background:#f6f8fb;border-top:3px solid {LAC};"><span style="display:block;font-size:30px;font-weight:bold;'
        f'color:{LAC};line-height:1.1;">{n}</span><span style="display:block;font-size:13px;color:#555;margin-top:4px;">{e(t)}</span></div>'
        for n, t in k) + '</div>'


def yayin_li(g, kendi=None):
    yz = ", ".join(f'<strong style="{UYE}">{e(a["n"])}</strong>' if a.get("m") and (kendi is None or a["n"] == kendi) else e(a["n"]) for a in g.get("authors") or [])
    kaynak = e(g.get("source") or "") + (f", {e(g['source_detail'])}" if g.get("source_detail") else "")
    s = f'<li style="margin:0 0 10px 0;line-height:1.55;">{yz} ({g.get("year")}). {e(g.get("title") or "")}. <em>{kaynak}</em>.'
    if g.get("doi"):
        s += f' <a href="https://doi.org/{e(g["doi"])}" target="_blank">DOI</a>'
    q = re.search(r"Q[1-4]", g.get("quartile") or "")
    if q:
        s += " " + etiket(q.group(0) + (f" (%{g['top_percent']})" if g.get("top_percent") else ""), Q_RENK[q.group(0)])
    return s + "</li>"


def satirlar(liste):
    return ('<table style="width:100%;border-collapse:collapse;font-size:15px;"><tbody>' + "".join(
        f'<tr><td style="width:95px;padding:6px 8px 6px 0;white-space:nowrap;color:#777;vertical-align:top;">{e(a)}</td>'
        f'<td style="padding:6px 0;vertical-align:top;">{b}</td></tr>' for a, b in liste) + '</tbody></table>')


def liste(items):
    return '<ol style="padding-left:22px;margin:0;">' + "".join(items) + '</ol>'


def li(t):
    return f'<li style="margin:0 0 9px 0;line-height:1.55;">{t}</li>'


def alt(t):
    return f'<h4 style="margin:18px 0 8px 0;color:#444;font-size:16px;">{e(t)}</h4>'


def yillara_gore(yayinlar):
    p, yil = [], None
    for g in yayinlar:
        if g.get("year") != yil:
            if yil is not None:
                p.append("</ol>")
            yil = g.get("year")
            p.append(f'<p style="margin:14px 0 6px 0;font-weight:bold;color:#666;">{yil}</p><ol style="padding-left:22px;margin:0;">')
        p.append(yayin_li(g, k["yazar_adi"]))
    if yil is not None:
        p.append("</ol>")
    return "".join(p)


def vurgula(yazarlar, k):
    return e(yazarlar).replace(e(k["yazar_adi"]), f'<strong style="{UYE}">{e(k["yazar_adi"])}</strong>')


def sayfa(k, yayinlar, projeler, logolar):
    benim = [g for g in yayinlar if any(a.get("m") and a.get("n") == k["yazar_adi"] for a in g.get("authors") or [])]
    p = []
    if k.get("ornek"):
        p.append('<div style="background:#fff8e1;border-left:4px solid #e0a800;padding:10px 14px;margin:0 0 22px 0;font-size:14px;color:#6b5300;">'
                 '<strong>Örnek sayfa.</strong> Scopus yayınları ve projeler gerçek, diğer bölümlerdeki bilgiler yerleşimi göstermek için örnek olarak yazılmıştır.</div>')
    p.append(ust(k, logolar))
    # 1. Özgeçmiş ve uzmanlık
    if k.get("ozgecmis"):
        p += [baslik("Özgeçmiş"), f'<p style="font-size:16px;line-height:1.7;text-align:left;margin:0 0 10px 0;">{e(k["ozgecmis"])}</p>']
    if k.get("uzmanlik"):
        p.append('<p style="margin:6px 0 0 0;">' + "".join(
            f'<span style="display:inline-block;margin:0 6px 6px 0;padding:3px 12px;border-radius:14px;background:#eef2f7;color:{LAC};font-size:14px;">{e(u)}</span>'
            for u in k["uzmanlik"]) + '</p>')
    # 3. Akademik ve idari geçmiş
    if k.get("akademik"):
        p += [baslik("Akademik Deneyim"), satirlar([(c, f'<strong>{e(a)}</strong><br><span style="color:#555;">{e(b)}</span>') for a, b, c in k["akademik"]])]
    if k.get("idari"):
        p += [baslik("İdari Deneyim"), satirlar([(c, f'<strong>{e(a)}</strong><br><span style="color:#555;">{e(b)}</span>') for a, b, c in k["idari"]])]
    # 2. Eğitim
    if k.get("egitim"):
        rows = []
        for d in k["egitim"]:
            duzey, kurum, yil = d[0], d[1], d[2] if len(d) > 2 else ""
            tez = d[3] if len(d) > 3 else ""
            dan = d[4] if len(d) > 4 else ""
            ek = (f'<br><span style="color:#555;">Tez: {e(tez)}</span>' if tez else "") + (f'<br><span style="color:#555;">Danışman: {e(dan)}</span>' if dan else "")
            rows.append((yil, f'<strong>{e(duzey)}</strong><br><span style="color:#555;">{e(kurum)}</span>{ek}'))
        p += [baslik("Eğitim"), satirlar(rows)]
    # 4. Yayınlar
    def el(d, tur_etiket=None):
        t = f'{vurgula(d["yazarlar"], k)} ({e(str(d["yil"]))}). {e(d["baslik"])}. <em>{e(d.get("kaynak", ""))}</em>'
        t += (f', {e(d["ayrinti"])}' if d.get("ayrinti") else "") + "."
        if d.get("doi"):
            t += f' <a href="https://doi.org/{e(d["doi"])}" target="_blank">DOI</a>'
        for fld, renk in (("metin", ("#f1f4f8", "#455a74")), ("sunum", ("#f3eef7", "#5f4a70"))):
            if d.get(fld):
                t += " " + etiket(d[fld], FORMAT_RENK.get(d[fld], GRI))
        for ind in d.get("indeks") or []:
            t += " " + etiket(ind, IND_RENK.get(ind, GRI))
        if tur_etiket:
            t += " " + etiket(tur_etiket, ("#eef2f7", "#4a5b70"))
        return li(t)

    def sirala(ogeler):
        return [h for _, h in sorted(ogeler, key=lambda x: x[0], reverse=True)]

    sc_mak = [g for g in benim if g.get("type") != "Bildiri"]
    ek_mak = k.get("uluslararasi_ek") or []
    ulusal = k.get("ulusal_yayinlar") or []
    kitap = k.get("kitaplar") or []
    n_ul = len(sc_mak) + len(ek_mak)
    if n_ul or ulusal or kitap:
        p.append(baslik("Yayınlar", n_ul + len(ulusal) + len(kitap)))
        if n_ul:
            p.append(alt(f"Uluslararası Hakemli Dergilerde Yayımlanan Makaleler ({n_ul})"))
            p.append(liste(sirala([(str(g.get("year")) + str(g.get("date") or ""), yayin_li(g, k["yazar_adi"])) for g in sc_mak]
                                  + [(str(d["yil"]), el(d)) for d in ek_mak])))
        if ulusal:
            p.append(alt(f"Ulusal Hakemli Dergilerde Yayımlanan Makaleler ({len(ulusal)})"))
            p.append(liste(sirala([(str(d["yil"]), el(d)) for d in ulusal])))
        if kitap:
            p.append(alt(f"Kitap Bölümleri ({len(kitap)})"))
            p.append(liste(sirala([(str(d["yil"]), el(d)) for d in kitap])))
    # 5. Bildiriler
    bild = k.get("bildiriler") or []
    sc_bild = [g for g in benim if g.get("type") == "Bildiri"]
    if bild or sc_bild:
        p.append(baslik("Bildiriler", len(bild) + len(sc_bild)))
        for kap in ["Uluslararası", "Ulusal"]:
            bu = [d for d in bild if d.get("kapsam") == kap]
            ek = sc_bild if kap == "Uluslararası" else []
            if bu or ek:
                p.append(alt(f"{kap} Bildiriler ({len(bu) + len(ek)})"))
                p.append(liste(sirala([(str(g.get("year")), yayin_li(g, k["yazar_adi"])) for g in ek] + [(str(d["yil"]), el(d)) for d in bu])))
    # 6. Projeler
    dur = {"Devam Ediyor": ("#e8eef8", "#17365d"), "Tamamlandı": ("#e3f2e6", "#2e6b3a")}
    def proje_li(x):
        yil = x.get("yillar") or x["yil"]
        return (str(x["yil"]), li(f'{e(x["baslik"])}. <em>{e(x.get("kaynak", ""))}</em>' + (f', {e(x["kod"])}' if x.get("kod") else "")
                + f' ({e(str(yil))}).' + (" " + etiket(x["rol"], ROL_RENK.get(x["rol"], DIGER_ROL)) if x.get("rol") else "")
                + (" " + etiket("Devam Ediyor", DEVAM) if str(x.get("durum", "")).lower().startswith("devam") else "")))

    if k.get("projeler_arastirma") or k.get("projeler_kus"):
        for anahtar, ad in (("projeler_arastirma", "Projeler (Araştırma)"), ("projeler_kus", "Projeler (Kamu-Üniversite-Sanayi)")):
            if k.get(anahtar):
                p.append(baslik(ad, len(k[anahtar])))
                p.append(liste(sirala([proje_li(x) for x in k[anahtar]])))
    else:
        pr = []
        for x in projeler:
            if k["ad"] not in str(x.get("team") or ""):
                continue
            r = re.search(re.escape(k["ad"]) + r"\s*\(([^)]+)\)", str(x["team"]))
            tarih = "–".join(dict.fromkeys(t[-4:] for t in [str(x.get("start") or ""), str(x.get("end") or "")] if t))
            kaynak = ", ".join(v for v in [e(x.get("funder") or ""), e(x.get("code") or "")] if v)
            pr.append((str(x.get("start") or "")[-4:], li(f'{e(x["title"])}. <em>{kaynak}</em>' + (f' ({tarih})' if tarih else '') + '.'
                       + (" " + etiket(r.group(1), ROL_RENK.get(r.group(1), DIGER_ROL)) if r else "")
                       + (" " + etiket("Devam Ediyor", DEVAM) if str(x.get("status", "")).lower().startswith("devam") else ""))))
        if pr:
            p.append(baslik("Projeler", len(pr)))
            p.append(liste(sirala(pr)))
    # 8. Editörlük ve hakemlik
    if k.get("editorluk") or k.get("hakemlik"):
        p.append(baslik("Editörlük ve Hakemlik"))
        if k.get("editorluk"):
            p.append(satirlar([(c, f'<strong>{e(a)}</strong><br><span style="color:#555;">{e(b)}</span>') for a, b, c in k["editorluk"]]))
        if k.get("hakemlik"):
            p.append(alt("Hakemlik Yapılan Dergiler")); p.append('<ul style="padding-left:22px;margin:0;">' + "".join(f'<li style="margin:0 0 4px 0;">{e(h)}</li>' for h in sorted(k["hakemlik"], key=str.casefold)) + "</ul>")
    # 9. Ödüller
    if k.get("oduller"):
        p += [baslik("Burslar, Eğitimler ve Ödüller"), satirlar([(a, f'<strong>{e(b)}</strong><br><span style="color:#555;">{e(c)}</span>') for a, b, c in sorted(k["oduller"], key=lambda x: str(x[0])[-4:], reverse=True)])]
    # 7. Tez danışmanlıkları
    tz = k.get("tezler") or []
    lt = k.get("lisans_tezleri") or {}
    if tz or lt:
        p.append(baslik("Tez Danışmanlıkları"))
        for duz in ["Doktora", "Yüksek Lisans"]:
            bu = [t for t in tz if t[0] == duz]
            if bu:
                p.append(alt(duz))
                p.append(liste([li(f'{e(o)}, <em>{e(b)}</em> ({e(y)}) · {e(d)}') for _, o, b, y, d in sorted(bu, key=lambda x: str(x[3]), reverse=True)]))
        if lt:
            p.append(alt("Lisans"))
            for donem in sorted(lt, key=str, reverse=True):
                p.append(f'<p style="margin:10px 0 4px 0;font-weight:bold;color:#666;">{e(str(donem))}</p>')
                p.append(liste([li(e(o) + (f': <em>{e(konu)}</em>' if konu else "")) for o, konu in lt[donem]]))
    p.append('<p style="margin:34px 0 0 0;"><a href="/kisiler">← Kişiler</a></p>')
    return '<div style="padding:10px 0 40px 0;">' + "".join(p) + '</div>'


def main():
    kisiler = yaml.safe_load((KOK / "_data/cv.yml").read_text(encoding="utf-8"))
    Y = yaml.safe_load((KOK / "_data/yayinlar.yml").read_text(encoding="utf-8"))
    Y = Y if isinstance(Y, list) else Y.get("yayinlar")
    P = yaml.safe_load((KOK / "_data/projeler.yml").read_text(encoding="utf-8")) or []
    logolar = {ad: LOGO.format(d) for ad, d in LOGO_AD.items()}
    for k in kisiler:
        yol = KOK / "sitefinity" / f'cv-{k["slug"]}.html'
        yol.write_text(sayfa(k, Y, P, logolar), encoding="utf-8")
        print("yazıldı", yol.name)


if __name__ == "__main__":
    main()
