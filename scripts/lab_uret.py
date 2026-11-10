"""Sitefinity laboratuvar sayfalarının içerik bloklarını üretir: sitefinity/lab-*.html
Şimdilik ÖRNEK içerik; gerçek cihaz listesi, fotoğraflar ve sorumlular gelince güncellenecek."""
import html
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
e = html.escape
LACIVERT = "#17365d"
LIB = "/images/librariesprovider187/default-album/"
ORNEK = ""  # "Örnek içerik" uyarısı 09.11.2026'da kullanıcı isteğiyle kaldırıldı

LABLAR = [
    {
        "kod": "kaya", "ad": "Kaya Mekaniği Laboratuvarı", "url": "/laboratuvar/kaya-mekanigi-laboratuvari",
        "gorsel": ("lab-kaya-mekanigi.jpg", "TomasSab, CC BY-SA 4.0",
                   "https://commons.wikimedia.org/wiki/File:Danish_triaxial_shear_test_apparatus,_in_action.jpg"),
        "kisa": "Kayaçların dayanım ve deformasyon özelliklerinin belirlendiği deneyler.",
        "tanitim": "Laboratuvarımızda kaya malzemesinin dayanım, deformasyon ve süreksizlik özelliklerini belirlemeye yönelik "
                   "deneyler yapılmaktadır. Laboratuvar lisans ve lisansüstü derslerde, tez çalışmalarında ve araştırma "
                   "projelerinde kullanılmaktadır.",
        "deneyler": [
            ("Tek eksenli basınç dayanımı ve deformabilite", "ISRM (1979), ASTM D7012", "Hidrolik pres, şekil değiştirme ölçerler"),
            ("Dolaylı (Brezilya) çekme dayanımı", "ISRM (1978), ASTM D3967", "Hidrolik pres, Brezilya çeneleri"),
            ("Nokta yükleme dayanım indeksi", "ISRM (1985), ASTM D5731", "Nokta yükleme cihazı"),
            ("Schmidt çekici sertliği", "ISRM (2009)", "L tipi Schmidt çekici"),
            ("Suda dağılmaya karşı duraylılık", "ISRM (1979), ASTM D4644", "Slake durability cihazı"),
            ("Ultrasonik ses hızı", "ISRM (2014)", "P ve S dalgası ölçüm cihazı"),
            ("Süreksizlik makaslama dayanımı", "ISRM (1974)", "Taşınabilir makaslama kutusu"),
        ],
        "sorumlu": "eklenecek",
    },
    {
        "kod": "indeks", "ad": "İndeks Özellikler Laboratuvarı", "url": "/laboratuvar/indeks-ozellikler-laboratuvari",
        "gorsel": ("lab-indeks-ozellikler.jpg", "Alandmanson, CC BY-SA 4.0",
                   "https://commons.wikimedia.org/wiki/File:Soil_fertility_analysis_5_Sample_dilution.jpg"),
        "kisa": "Kaya ve zeminlerin fiziksel ve indeks özelliklerinin belirlenmesi.",
        "tanitim": "Laboratuvarımızda kaya ve zemin örneklerinin yoğunluk, porozite, su emme ve kıvam gibi indeks özellikleri "
                   "belirlenmektedir. Bu deneyler mühendislik sınıflamalarının ve diğer deneylerin temelini oluşturur.",
        "deneyler": [
            ("Birim hacim ağırlık, porozite ve su emme", "ISRM (1979), TS EN 1936, TS EN 13755", "Etüv, hassas terazi, vakum düzeneği"),
            ("Özgül ağırlık", "ASTM D854", "Piknometre"),
            ("Kıvam (Atterberg) limitleri", "ASTM D4318", "Casagrande aleti"),
            ("Dane boyu dağılımı", "ASTM D6913", "Elek takımı, sarsma makinesi"),
            ("Su içeriği", "ASTM D2216", "Etüv, hassas terazi"),
        ],
        "sorumlu": "eklenecek",
    },
    {
        "kod": "hidro", "ad": "Hidrojeoloji Laboratuvarı", "url": "/laboratuvar/hidrojeoloji-laboratuvari",
        "gorsel": ("lab-hidrojeoloji.jpg", "U.S. Department of Energy, kamu malı",
                   "https://commons.wikimedia.org/wiki/File:UMTRAP_42_010_(26894061153).jpg"),
        "kisa": "Yeraltı suyu ölçümleri, su örneklemesi ve hidrolik iletkenlik deneyleri.",
        "tanitim": "Laboratuvarımızda yeraltı suyu ve yüzey suyu örneklerinin fiziksel ve kimyasal özellikleri ile zemin ve "
                   "kayaçların hidrolik iletkenliği belirlenmektedir. Arazi ölçüm ekipmanı saha çalışmalarında da "
                   "kullanılmaktadır.",
        "deneyler": [
            ("Hidrolik iletkenlik (sabit ve düşen seviyeli)", "ISO 17892-11", "Permeametre düzenekleri"),
            ("Esnek çeperli permeabilite", "ASTM D5084", "Esnek çeperli permeametre"),
            ("Arazi parametreleri (pH, EC, sıcaklık, çözünmüş oksijen)", "Üretici yöntemleri", "Çok parametreli prob"),
            ("Yeraltı suyu seviye ölçümü", "-", "Kuyu seviye ölçer, veri kaydedici"),
            ("Su örneklemesi", "ISO 5667-11", "Bailer, örnekleme pompası"),
        ],
        "sorumlu": "eklenecek",
    },
]


def gorsel(g):
    dosya, kredi, kaynak = g
    return (f'<img src="{LIB}{dosya}" alt="" style="display:block;width:100%;height:auto;" />'
            f'<p style="margin:3px 0 0 0;text-align:right;font-size:10px;line-height:1.2;color:#999;">'
            f'Görsel: <a href="{kaynak}" target="_blank" style="color:#999;">{e(kredi)}</a></p>')


def kapsayici(icerik):
    return f'<div style="padding:10px 0 40px 0;">{icerik}</div>'


def ana_sayfa():
    p = [ORNEK,
         '<p style="font-size:16px;line-height:1.7;color:#333;text-align:justify;margin:0 0 26px 0;">'
         'Çalışma grubumuz bünyesinde kaya mekaniği, indeks özellikler ve hidrojeoloji alanlarında üç laboratuvar '
         'bulunmaktadır. Laboratuvarlar lisans ve lisansüstü eğitimde, tez çalışmalarında ve araştırma projelerinde '
         'kullanılmaktadır.</p>', '<div>']
    for lab in LABLAR:
        p.append(f'<div style="display:inline-block;vertical-align:top;width:31%;min-width:240px;margin:0 2% 22px 0;'
                 f'background:#fafafa;border-top:4px solid {LACIVERT};">'
                 f'<a href="{lab["url"]}">{gorsel(lab["gorsel"])}</a>'
                 f'<div style="padding:12px 16px 16px 16px;">'
                 f'<p style="margin:0 0 8px 0;font-size:18px;font-weight:bold;"><a href="{lab["url"]}" style="color:{LACIVERT};text-decoration:none;">{e(lab["ad"])}</a></p>'
                 f'<p style="margin:0 0 10px 0;font-size:14px;line-height:1.6;color:#444;">{e(lab["kisa"])}</p>'
                 f'<p style="margin:0;font-size:13px;"><a href="{lab["url"]}">Laboratuvarı incele →</a></p></div></div>')
    p.append('</div>')
    p.append('<p style="margin:16px 0 0 0;font-size:14px;color:#555;"><strong>Konum:</strong> İTÜ Ayazağa Kampüsü, Maden Fakültesi '
             '(bina ve oda bilgisi eklenecek)</p>')
    return kapsayici("".join(p))


def lab_sayfasi(lab):
    satirlar = "".join(
        f'<tr><td style="padding:8px 10px;border-bottom:1px solid #e3e8ef;">{e(ad)}</td>'
        f'<td style="padding:8px 10px;border-bottom:1px solid #e3e8ef;color:#555;">{e(std)}</td>'
        f'<td style="padding:8px 10px;border-bottom:1px solid #e3e8ef;color:#555;">{e(cihaz)}</td></tr>'
        for ad, std, cihaz in lab["deneyler"])
    th = f'style="text-align:left;padding:8px 10px;background:{LACIVERT};color:#fff;font-weight:normal;"'
    p = [ORNEK,
         '<div>',
         f'<div style="display:inline-block;vertical-align:top;width:48%;min-width:280px;margin:0 3% 20px 0;">{gorsel(lab["gorsel"])}</div>',
         f'<div style="display:inline-block;vertical-align:top;width:48%;min-width:280px;">'
         f'<p style="font-size:16px;line-height:1.7;color:#333;text-align:justify;margin:0 0 16px 0;">{e(lab["tanitim"])}</p>'
         f'<p style="margin:0 0 6px 0;font-size:14px;"><strong>Sorumlu öğretim üyesi:</strong> {e(lab["sorumlu"])}</p>'
         f'<p style="margin:0 0 6px 0;font-size:14px;"><strong>Konum:</strong> bina ve oda bilgisi eklenecek</p>'
         f'<p style="margin:0;font-size:14px;"><strong>İletişim:</strong> e-posta eklenecek</p></div>',
         '</div>',
         f'<h3 style="margin:30px 0 14px 0;padding-bottom:8px;border-bottom:2px solid #e3e8ef;">Yapılan Deneyler</h3>',
         f'<div style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;font-size:14px;"><thead><tr>'
         f'<th {th}>Deney</th><th {th}>Standart</th><th {th}>Cihaz</th></tr></thead><tbody>{satirlar}</tbody></table></div>',
         f'<h3 style="margin:34px 0 14px 0;padding-bottom:8px;border-bottom:2px solid #e3e8ef;">Fotoğraflar</h3>',
         '<div>' + "".join(
             '<div style="display:inline-block;width:23%;min-width:150px;margin:0 2% 12px 0;background:#eef1f5;'
             'color:#99a;font-size:13px;text-align:center;padding:48px 0;">Fotoğraf eklenecek</div>' for _ in range(4)) + '</div>',
         f'<h3 style="margin:34px 0 14px 0;padding-bottom:8px;border-bottom:2px solid #e3e8ef;">Dış Hizmet</h3>',
         '<p style="font-size:15px;line-height:1.7;color:#333;margin:0;">Laboratuvarımızda kurum dışı talepler için deney '
         'hizmeti verilip verilmediği ve başvuru süreci bu bölümde açıklanacaktır.</p>',
         '<p style="margin:26px 0 0 0;"><a href="/laboratuvar">← Tüm laboratuvarlar</a></p>']
    return kapsayici("".join(p))


def main():
    cikti = KOK / "sitefinity"
    (cikti / "lab-ana.html").write_text(ana_sayfa(), encoding="utf-8")
    for lab in LABLAR:
        (cikti / f'lab-{lab["kod"]}.html').write_text(lab_sayfasi(lab), encoding="utf-8")
    print("tamam")


if __name__ == "__main__":
    main()
