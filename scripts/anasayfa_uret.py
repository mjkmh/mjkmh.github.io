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
KISI_SAYISI = 12
PROJE_SAYISI = 4


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
<p style="margin:0 0 14px 0;font-size:16px;line-height:1.65;color:#333;text-align:justify;">Kökleri İTÜ’de yerbilimleri eğitiminin kurulduğu yıllara uzanan grubumuz; kaya ve zeminlerin mühendislik davranışı, şev ve heyelan tehlikesi, yeraltı suyu ve kültürel miras yapı taşları üzerine deneysel, sayısal ve saha tabanlı araştırmalar yürütmektedir.</p>
<p style="margin:0;"><a href="/hakkimizda" style="display:inline-block;padding:8px 18px;background:{LACIVERT};color:#fff;text-decoration:none;border-radius:4px;margin:0 8px 8px 0;">Dünden Bugüne MJKMH</a><a href="/kisiler" style="display:inline-block;padding:7px 17px;border:1px solid {LACIVERT};color:{LACIVERT};text-decoration:none;border-radius:4px;margin:0 0 8px 0;">Kişiler</a></p>
</td>
<td style="vertical-align:middle;padding:0;"><img src="{GORSEL}" alt="Kaya şevi" style="width:100%;height:auto;display:block;border-radius:6px;" /></td>
</tr></tbody></table>'''


def rakamlar(say, toplam):
    kutular = [(say["makale"], "Makale", "/yayinlar"), (say["ilk10"], "İlk %10’luk Dilimdeki Makale", "/yayinlar"),
               (say["Q1"], "Q1 Makale", "/yayinlar"), (PROJE_SAYISI, "Proje", "/projeler"),
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
    ("Mühendislik Jeolojisi", "undul-2026-kaya-dusmesi.jpg", "Heyelan ve kaya düşmesi tehlikesi, CBS tabanlı tehlike haritalaması, zemin iyileştirme ve altyapı projelerinde jeolojik değerlendirme."),
    ("Kaya Mekaniği", "undul-2026-bonded-particle.jpg", "Kayaçların dayanım ve deformasyon davranışı, çatlak başlangıcı, parçacık tabanlı sayısal modelleme, tünel ve şev stabilitesi."),
    ("Hidrojeoloji", "dinc-gogus-2026-fraktal.jpg", "Yeraltı suyu akımı ve kalitesi, kirletici taşınımı, akifer karakterizasyonu ve su–kaya etkileşimi."),
]


def alanlar():
    p = [baslik("Çalışma Alanlarımız"),
         '<table style="width:100%;border-collapse:separate;border-spacing:12px 0;border:0;margin:0 -12px;"><tbody><tr>']
    for ad, gorsel, metin in ALANLAR:
        p.append(f'<td style="width:33%;vertical-align:top;border-top:4px solid {LACIVERT};background:#fafafa;padding:0 0 16px 0;">'
                 f'<img src="{IMG}{gorsel}" alt="{e(ad)}" style="display:block;width:100%;height:150px;object-fit:cover;margin:0 0 14px 0;" />'
                 f'<div style="padding:0 18px;">'
                 f'<p style="margin:0 0 8px 0;font-size:18px;font-weight:bold;color:{LACIVERT};">{e(ad)}</p>'
                 f'<p style="margin:0;font-size:14px;line-height:1.6;color:#444;">{e(metin)}</p></div></td>')
    p.append('</tr></tbody></table>')
    return "".join(p)


PROJELER = [
    ("TÜBİTAK 1001", "İstanbul’un Kültürel Miras Yapılarında Kullanılan Taşlar İçin Alternatif Kaynakların Belirlenmesine Yönelik Veri Tabanlı Uyumluluk İndeksi ve Deneysel Sistematiğin Geliştirilmesi", "126M496"),
    ("İTÜ BAP – Hızlı Destek", "Sedimanter Kaya Malzemelerinde Çatlak Başlangıcı Gerilmesinin Parçacık Tabanlı Sayısal Modellemesinde Bağ Modellerinin Karşılaştırmalı Analizi", "2026"),
    ("İTÜ BAP – Araştırmaya Başlangıç", "D-650 Karayolunun Arifiye-Bozüyük Kesimindeki Heyelan Tehlikesinin AHP ve CBS Tabanlı Yöntemlerle Değerlendirilmesi", "2025–2027"),
]


def projeler():
    rozet = "display:inline-block;font-size:12px;padding:0 7px;margin-right:4px;"
    p = [baslik("Devam Eden Projeler", "/projeler", "Tüm projeler")]
    for tur, ad, ek in PROJELER:
        p.append(f'<div style="border-left:4px solid {LACIVERT};background:#fafafa;padding:12px 16px;margin:0 0 12px 0;">'
                 f'<p style="margin:0 0 5px 0;"><span style="{rozet}border:1px solid #bbb;color:#555;">{e(tur)}</span>'
                 f'<span style="{rozet}border:1px solid {LACIVERT};color:{LACIVERT};">Devam ediyor</span>'
                 f'<span style="font-size:12px;color:#888;">{e(ek)}</span></p>'
                 f'<p style="margin:0;font-size:15px;line-height:1.4;"><strong>{e(ad)}</strong></p></div>')
    return "".join(p)


def son_yayinlar(girdiler, n=4):
    sirali = sorted(girdiler, key=lambda g: str(g.get("date") or g.get("year")), reverse=True)[:n]
    p = [baslik("Son Yayınlar", "/yayinlar", "Tüm yayınlar"), '<ul style="list-style:none;margin:0;padding:0;">']
    for g in sirali:
        yz = ", ".join(f'<strong style="{UYE}">{e(a["n"])}</strong>' if a.get("m") else e(a["n"])
                       for a in g.get("authors") or [])
        s = (f'<li style="margin:0 0 14px 0;padding:0 0 14px 0;border-bottom:1px solid #eee;line-height:1.55;">'
             f'<span style="font-size:15px;"><strong>{e(g.get("title") or "")}</strong></span><br />'
             f'<span style="font-size:13px;color:#555;">{yz} ({g.get("year")}) · <em>{e(g.get("source") or "")}</em></span>')
        if g.get("type"):
            s += " " + etiket(g["type"], TUR_RENK.get(g["type"], ("#f1f1f1", "#555")))
        q = re.search(r"Q[1-4]", g.get("quartile") or "")
        if q:
            s += " " + etiket(q.group(0) + (f" (%{g['top_percent']})" if g.get("top_percent") else ""), Q_RENK[q.group(0)])
        if g.get("doi"):
            s += f' <a href="https://doi.org/{e(g["doi"])}" target="_blank" style="font-size:13px;">DOI</a>'
        p.append(s + "</li>")
    p.append("</ul>")
    return "".join(p)


HABERLER = [
    ("angi-2026-kufeki.jpg", "05.11.2026", "[Örnek] TÜBİTAK 1001 projemiz için bursiyer alımı başladı", "Kültürel miras yapı taşları projemizde görev alacak lisans, yüksek lisans ve doktora bursiyerleri aranıyor."),
    ("bozkurtoglu-2026-kazi.jpg", "20.10.2026", "[Örnek] Arazi çalışması: İstanbul kazı şevlerinde ölçümler", "Ekibimiz İstanbul’daki derin kazılarda süreksizlik ölçümleri ve numune alımı gerçekleştirdi."),
    ("zengin-2026-yesil-alan.jpg", "15.09.2026", "[Örnek] EUROCK 2026’da iki bildiri sunduk", "Üsküp’te düzenlenen sempozyumda grubumuzun çalışmaları sözlü ve poster olarak sunuldu."),
]


def haberler():
    p = [baslik("Haberler ve Duyurular"),
         '<table style="width:100%;border-collapse:separate;border-spacing:12px 0;border:0;margin:0 -12px;"><tbody><tr>']
    for gorsel, tarih, ad, ozet in HABERLER:
        p.append(f'<td style="width:33%;vertical-align:top;background:#fff;border:1px solid #e3e8ef;padding:0 0 14px 0;">'
                 f'<img src="{IMG}{gorsel}" alt="" style="display:block;width:100%;height:170px;object-fit:cover;margin:0 0 12px 0;" />'
                 f'<div style="padding:0 16px;"><p style="margin:0 0 6px 0;font-size:12px;color:#888;">{tarih}</p>'
                 f'<p style="margin:0 0 8px 0;font-size:16px;line-height:1.35;font-weight:bold;color:{LACIVERT};">{e(ad)}</p>'
                 f'<p style="margin:0;font-size:14px;line-height:1.55;color:#444;">{e(ozet)}</p></div></td>')
    p.append('</tr></tbody></table>')
    return "".join(p)


def main():
    girdiler = yaml.safe_load((KOK / "_data/yayinlar.yml").read_text(encoding="utf-8"))
    parcalar = [giris(), rakamlar(istatistik(girdiler), len(girdiler)), alanlar(), son_yayinlar(girdiler), projeler(), haberler()]
    yol = KOK / "sitefinity/anasayfa.html"
    yol.write_text("<div>" + "\n".join(parcalar) + "</div>", encoding="utf-8")
    print(yol)


if __name__ == "__main__":
    main()
