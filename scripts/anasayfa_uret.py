"""Sitefinity ana sayfa içerik bloğunu üretir: sitefinity/anasayfa.html
Yayın istatistikleri ve son yayınlar _data/yayinlar.yml'den okunur (scopus_guncelle.py sonrası çalıştırılır)."""
import html, re, sys
from pathlib import Path
import yaml

KOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))
from scopus_guncelle import istatistik, etiket, TUR_RENK, Q_RENK, UYE  # noqa: E402

e = html.escape
LACIVERT = "#17365d"
GORSEL = "/images/librariesprovider187/default-album/anasayfa-kaya-sevi.jpg?sfvrsn=352c804_2"


def baslik(metin, link=None, link_yazi=None):
    sag = (f'<a href="{link}" style="float:right;font-size:14px;font-weight:normal;margin-top:6px;">'
           f'{link_yazi} →</a>') if link else ""
    return (f'<h3 style="margin:46px 0 16px 0;padding-bottom:8px;border-bottom:2px solid #e3e8ef;">'
            f'{sag}{e(metin)}</h3>')


def giris():
    return f'''<table style="width:100%;border-collapse:collapse;border:0;"><tbody><tr>
<td style="width:55%;vertical-align:middle;padding:0 28px 0 0;">
<p style="margin:0 0 6px 0;font-size:13px;letter-spacing:1px;color:#777;">İTÜ MADEN FAKÜLTESİ · JEOLOJİ MÜHENDİSLİĞİ BÖLÜMÜ</p>
<p style="margin:0 0 16px 0;font-size:30px;line-height:1.2;font-weight:bold;color:{LACIVERT};">Mühendislik Jeolojisi – Kaya Mekaniği – Hidrojeoloji Çalışma Grubu</p>
<p style="margin:0 0 14px 0;font-size:16px;line-height:1.65;color:#333;text-align:justify;">Kökleri İTÜ’de yerbilimleri eğitiminin kurulduğu yıllara uzanan grubumuz, kaya ve zeminlerin mühendislik davranışı, şev ve heyelan tehlikesi, yeraltı suyu ve kültürel miras yapı taşları üzerine deneysel, sayısal ve saha tabanlı araştırmalar yürütmektedir.</p>
<p style="margin:0;"><a href="/hakkimizda" style="display:inline-block;padding:8px 18px;background:{LACIVERT};color:#fff;text-decoration:none;border-radius:4px;margin:0 8px 8px 0;">Dünden Bugüne MJKMH</a><a href="/kisiler" style="display:inline-block;padding:7px 17px;border:1px solid {LACIVERT};color:{LACIVERT};text-decoration:none;border-radius:4px;margin:0 0 8px 0;">Kişiler</a></p>
</td>
<td style="vertical-align:middle;padding:0;"><img src="{GORSEL}" alt="Kaya şevi" style="width:100%;height:auto;display:block;border-radius:6px;" /></td>
</tr></tbody></table>'''


def rakamlar(say, toplam):
    import yaml
    KISI_SAYISI = len(yaml.safe_load((KOK / "_data/aktif_uyeler.yml").read_text(encoding="utf-8")) or [])
    PROJE_SAYISI = sum(1 for x in yaml.safe_load((KOK / "_data/projeler.yml").read_text(encoding="utf-8")) or []
                       if str(x.get("status", "")).startswith("Devam"))
    kutular = [(say["makale"], "Makale", "/yayinlar"), (say["ilk10"], "İlk %10’luk Dilimdeki Makale", "/yayinlar"),
               (say["Q1"], "Q1 Makale", "/yayinlar"), (PROJE_SAYISI, "Devam Eden Proje", "/projeler"),
               (KISI_SAYISI, "Araştırmacı", "/kisiler")]
    p = ['<table style="width:100%;border-collapse:separate;border-spacing:10px 0;margin:34px 0 0 0;border:0;"><tbody><tr>']
    for n, ad, link in kutular:
        p.append(f'<td style="width:20%;text-align:center;background:#f3f6fa;border-radius:8px;padding:16px 6px;">'
                 f'<a href="{link}" style="text-decoration:none;color:{LACIVERT};">'
                 f'<span style="display:block;font-size:30px;font-weight:bold;line-height:1.1;">{n}</span>'
                 f'<span style="display:block;font-size:13px;color:#555;margin-top:4px;">{e(ad)}</span></a></td>')
    p.append('</tr></tbody></table>')
    return "".join(p)


IMG = "https://mjkmh.github.io/images/yayinlar/"
ALANLAR = [
    ("Mühendislik Jeolojisi", ("/images/librariesprovider187/default-album/alan-muhendislik-jeolojisi.jpg", "Wikimedia Commons, CC BY-SA 3.0", "https://commons.wikimedia.org/wiki/File:Landslide_on_Karakoram_Highway_in_Pakistan.jpg"), "Heyelan ve kaya düşmesi tehlikesi, CBS tabanlı tehlike haritalaması, zemin iyileştirme ve altyapı projelerinde jeolojik değerlendirme."),
    ("Kaya Mekaniği", ("/images/librariesprovider187/default-album/alan-kaya-mekanigi.jpg", "Graeme Churchard, CC BY 2.0", "https://commons.wikimedia.org/wiki/File:Jointed_turbidite_outcrop_at_Randa,_Mallorca.jpg"), "Kayaçların dayanım ve deformasyon davranışı, çatlak başlangıcı, parçacık tabanlı sayısal modelleme, tünel ve şev stabilitesi."),
    ("Hidrojeoloji", ("/images/librariesprovider187/default-album/alan-hidrojeoloji.jpg", "Günter Herrmann, CC BY-SA 3.0 de", "https://commons.wikimedia.org/wiki/File:Quelltopf-Grimmensee_Langenauer-Ried_Karstquelle_Schwaebische-Alb.jpg"), "Yeraltı suyu akımı ve kalitesi, kirletici taşınımı, akifer karakterizasyonu ve su–kaya etkileşimi."),
]


def gorsel_html(g, yukseklik=None, link=None):
    """Görseller önceden 4:3 kırpılıp kütüphaneye yüklendi; doğal oranında gösterilir, sündürülmez."""
    url, kredi, kaynak = g
    img = f'<img src="{url}" alt="" style="display:block;width:100%;height:auto;" />'
    if link:
        img = f'<a href="{link}">{img}</a>'
    return (img + f'<p style="margin:3px 8px 10px 0;text-align:right;font-size:10px;line-height:1.2;color:#999;">'
            f'Görsel: <a href="{kaynak}" target="_blank" style="color:#999;">{e(kredi)}</a></p>')


def alanlar():
    p = [baslik("Çalışma Alanlarımız"),
         '<table style="width:100%;border-collapse:separate;border-spacing:12px 0;border:0;margin:0 -12px;"><tbody><tr>']
    for ad, gorsel, metin in ALANLAR:
        p.append(f'<td style="width:33%;vertical-align:top;border-top:4px solid {LACIVERT};background:#fafafa;padding:0 0 16px 0;">' +
                 gorsel_html(gorsel, 160) +
                 f'<div style="padding:0 18px;">'
                 f'<p style="margin:0 0 8px 0;font-size:18px;font-weight:bold;color:{LACIVERT};">{e(ad)}</p>'
                 f'<p style="margin:0;font-size:14px;line-height:1.6;color:#444;">{e(metin)}</p></div></td>')
    p.append('</tr></tbody></table>')
    return "".join(p)


def projeler():
    import yaml
    P = yaml.safe_load((KOK / "_data/projeler.yml").read_text(encoding="utf-8")) or []
    son = sorted(P, key=lambda x: str(x.get("start") or "")[-4:], reverse=True)[:5]
    p = [baslik("Son Projeler", "/projeler", "Tüm projeler"), '<ul style="list-style:none;margin:0;padding:0;">']
    for x in son:
        yil = "–".join(dict.fromkeys(t[-4:] for t in [str(x.get("start") or ""), str(x.get("end") or "")] if t))
        bilgi = " · ".join(v for v in [e(x.get("funder") or ""), e(x.get("code") or ""), yil] if v)
        yur = [t.strip() for t in str(x.get("team") or "").split(",") if "Yürütücü" in t]
        ekip = f' · {e(yur[0])}' if yur else ""
        p.append(f'<li style="margin:0 0 14px 0;padding:0 0 14px 0;border-bottom:1px solid #eee;line-height:1.55;">'
                 f'<span style="font-size:15px;"><strong>{e(x["title"])}</strong></span><br />'
                 f'<span style="font-size:13px;color:#555;">{bilgi}{ekip}</span> '
                 + (etiket("Devam Ediyor", ("#e3f0fb", "#1f5fa8")) if str(x.get("status", "")).startswith("Devam") else "") + '</li>')
    p.append("</ul>")
    return "".join(p)


def son_yayinlar(girdiler, n=5, bildiri=False):
    sec = [g for g in girdiler if (g.get("type") == "Bildiri") == bildiri]
    sirali = sorted(sec, key=lambda g: str(g.get("date") or g.get("year")), reverse=True)[:n]
    p = [baslik("Son Bildiriler" if bildiri else "Son Yayınlar", "/yayinlar", "Tüm yayınlar"), '<ul style="list-style:none;margin:0;padding:0;">']
    for g in sirali:
        yz = ", ".join(f'<strong style="{UYE}">{e(a["n"])}</strong>' if a.get("m") else e(a["n"])
                       for a in g.get("authors") or [])
        s = (f'<li style="margin:0 0 14px 0;padding:0 0 14px 0;border-bottom:1px solid #eee;line-height:1.55;">'
             f'<span style="font-size:15px;"><strong>{e(g.get("title") or "")}</strong></span><br />'
             f'<span style="font-size:13px;color:#555;">{yz} ({g.get("year")}) · <em>{e(g.get("source") or "")}</em></span>')
        q = re.search(r"Q[1-4]", g.get("quartile") or "")
        if q:
            s += " " + etiket(q.group(0) + (f" (%{g['top_percent']})" if g.get("top_percent") else ""), Q_RENK[q.group(0)])
        if g.get("doi"):
            s += f' <a href="https://doi.org/{e(g["doi"])}" target="_blank" style="font-size:13px;">DOI</a>'
        p.append(s + "</li>")
    p.append("</ul>")
    return "".join(p)


HABERLER = [
    (("/images/librariesprovider187/default-album/haber-bursiyer-4x3.jpg", "Silvia Forti, CC0", "https://commons.wikimedia.org/wiki/File:GeologyGarda4.jpg"), "05.11.2026", "/haber-detay/2026/11/05/örnek-tübi-tak-1001-projemiz-için-bursiyer-alımı-başladı", "[Örnek] TÜBİTAK 1001 projemiz için bursiyer alımı başladı", "Kültürel miras yapı taşları projemizde görev alacak lisans, yüksek lisans ve doktora bursiyerleri aranıyor."),
    (("/images/librariesprovider187/default-album/haber-arazi-4x3.jpg", "Joseph H. Hartman, CC0", "https://commons.wikimedia.org/wiki/File:Judson_Locality_(GeoDIL_number_-_1947).jpg"), "05.11.2026", "/haber-detay/2026/11/05/örnek-arazi-çalışması-i-stanbul-kazı-şevlerinde-ölçümler", "[Örnek] Arazi çalışması: İstanbul kazı şevlerinde ölçümler", "Ekibimiz İstanbul’daki derin kazılarda süreksizlik ölçümleri ve numune alımı gerçekleştirdi."),
    (("/images/librariesprovider187/default-album/haber-eurock-4x3.jpg", "Julian Nyča, CC BY-SA 3.0", "https://commons.wikimedia.org/wiki/File:Skopje_%E2%80%93_Vardar_Bridge_(2017).jpg"), "05.11.2026", "/haber-detay/2026/11/05/örnek-eurock-2026-da-iki-bildiri-sunduk", "[Örnek] EUROCK 2026’da iki bildiri sunduk", "Üsküp’te düzenlenen sempozyumda grubumuzun çalışmaları sözlü ve poster olarak sunuldu."),
]


def haberler():
    p = [baslik("Haberler ve Duyurular", "/haberler", "Tüm haberler"),
         '<table style="width:100%;border-collapse:separate;border-spacing:12px 0;border:0;margin:0 -12px;"><tbody><tr>']
    for gorsel, tarih, link, ad, ozet in HABERLER:
        p.append(f'<td style="width:33%;vertical-align:top;background:#fff;border:1px solid #e3e8ef;padding:0 0 14px 0;">' +
                 gorsel_html(gorsel, 170, link) +
                 f'<div style="padding:0 16px;"><p style="margin:0 0 6px 0;font-size:12px;color:#888;">{tarih}</p>'
                 f'<p style="margin:0 0 8px 0;font-size:16px;line-height:1.35;font-weight:bold;"><a href="{link}" style="color:{LACIVERT};text-decoration:none;">{e(ad)}</a></p>'
                 f'<p style="margin:0 0 8px 0;font-size:14px;line-height:1.55;color:#444;">{e(ozet)}</p>'
                 f'<p style="margin:0;font-size:13px;"><a href="{link}">Devamı →</a></p></div></td>')
    p.append('</tr></tbody></table>')
    return "".join(p)


def main():
    girdiler = yaml.safe_load((KOK / "_data/yayinlar.yml").read_text(encoding="utf-8"))
    parcalar = [giris(), rakamlar(istatistik(girdiler), len(girdiler)), alanlar(), son_yayinlar(girdiler), son_yayinlar(girdiler, bildiri=True), projeler(), haberler()]
    yol = KOK / "sitefinity/anasayfa.html"
    yol.write_text("<div>" + "\n".join(parcalar) + "</div>", encoding="utf-8")
    print(yol)


if __name__ == "__main__":
    main()
