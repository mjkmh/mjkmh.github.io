"""TR CV içerik bloklarından İngilizce sürüm üretir: sitefinity/cv-<slug>-en.html
Yayın ve tez başlıkları özgün dillerinde bırakılır; başlıklar, etiketler, kurumlar ve proje adları çevrilir."""
import json, re
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
S = {
    # bölüm başlıkları ve etiketler
    "Özgeçmiş": "Biography", "Akademik Deneyim": "Academic Experience", "İdari Deneyim": "Administrative Experience",
    "Eğitim": "Education", "Yayınlar": "Publications", "Bildiriler": "Conference Papers",
    "Projeler (Araştırma)": "Projects (Research)", "Projeler (Kamu-Üniversite-Sanayi)": "Projects (Public–University–Industry)",
    "Projeler": "Projects", "Editörlük ve Hakemlik": "Editorial and Reviewing Activities",
    "Hakemlik Yapılan Dergiler": "Journals Reviewed For", "Burslar, Eğitimler ve Ödüller": "Fellowships, Training and Awards",
    "Tez Danışmanlıkları": "Thesis Supervision", "Uluslararası Hakemli Dergilerde Yayımlanan Makaleler": "Articles in International Peer-Reviewed Journals",
    "Ulusal Hakemli Dergilerde Yayımlanan Makaleler": "Articles in National Peer-Reviewed Journals",
    "Kitap Bölümleri": "Book Chapters", "Uluslararası Bildiriler": "International Conference Papers", "Ulusal Bildiriler": "National Conference Papers",
    "← Kişiler": "← People", "Tam metin": "Full text", "Özet": "Abstract", "Sözlü": "Oral", "Devam Ediyor": "Ongoing",
    "Yürütücü": "PI", "Araştırmacı": "Researcher", "Tez: ": "Thesis: ", "Danışman: ": "Supervisor: ",
    "Scopus’tan otomatik olarak alınmaktadır. Q değerleri derginin güncel Scopus CiteScore dilimine göredir.":
        "Retrieved automatically from Scopus. Quartiles are based on the journal’s current Scopus CiteScore percentile.",
    "İTÜ Maden Fakültesi, Jeoloji Mühendisliği Bölümü": "ITU Faculty of Mines, Department of Geological Engineering",
    # unvanlar ve dereceler
    "Dr. Öğr. Üyesi": "Asst. Prof. Dr.", "Arş. Gör. Dr.": "Res. Asst. Dr.", "Arş. Gör.": "Res. Asst.", "Doç. Dr.": "Assoc. Prof. Dr.",
    "Post Doktora": "Postdoc", "Doktora Sırası Araştırmacı": "Visiting PhD Researcher", "Doktora Sonrası Araştırmacı": "Postdoctoral Researcher",
    "Doktora Sırası": "Visiting PhD", "Doktora": "PhD", "Yüksek Lisans": "MSc", "Lisans": "BSc",
    "Editör": "Editor", "Değerlendirici": "Evaluator", "Üye": "Member", "Koordinatör Yardımcısı": "Deputy Coordinator",
    "Koordinatör": "Coordinator", "Araştırma-Geliştirme Koordinatörü": "R&D Coordinator",
    # kurumlar
    "Jeoloji Mühendisliği Anabilim Dalı, Fen Bilimleri Enstitüsü": "Department of Geological Engineering, Graduate School of Natural and Applied Sciences",
    "Jeoloji Mühendisliği Bölümü, Maden Fakültesi": "Department of Geological Engineering, Faculty of Mines",
    "Jeoloji Mühendisliği Bölümü, Mühendislik Fakültesi": "Department of Geological Engineering, Faculty of Engineering",
    "Şehir ve Bölge Planlama Bölümü, Mimarlık Fakültesi": "Department of City and Regional Planning, Faculty of Architecture",
    "Maden Fakültesi, İstanbul Teknik Üniversitesi": "Faculty of Mines, Istanbul Technical University",
    "Lisansüstü Eğitimde Sürekli Kalite İyileştirme Komisyonu": "Graduate Education Continuous Quality Improvement Commission",
    "Araştırma-Geliştirme Alt Çalışma Grubu, Kalite Komisyonu": "R&D Sub-Working Group, Quality Commission",
    "Bilimsel Araştırma Projeleri Koordinasyon Birimi": "Scientific Research Projects Coordination Unit",
    "Kalite Komisyonu": "Quality Commission", "ABET Komisyonu": "ABET Commission",
    "Yükseköğretim Kalite Kurulu": "Higher Education Quality Council (YÖKAK)",
    "İstanbul Teknik Üniversitesi": "Istanbul Technical University", "Kütahya Dumlupınar Üniversitesi": "Kütahya Dumlupınar University",
    "Kocaeli Üniversitesi": "Kocaeli University", "Karadeniz Teknik Üniversitesi": "Karadeniz Technical University",
    "Hacettepe Üniversitesi": "Hacettepe University", "Çanakkale Onsekiz Mart Üniversitesi": "Çanakkale Onsekiz Mart University",
    "Akdeniz Üniversitesi": "Akdeniz University", "İstanbul Üniversitesi": "Istanbul University",
    "(Birleşik Krallık)": "(United Kingdom)", "(Kanada)": "(Canada)", "Belçika)": "Belgium)", "(Suudi Arabistan)": "(Saudi Arabia)",
    "DSİ Teknik Bülteni": "DSİ Technical Bulletin",
    "TÜBİTAK 2219 Yurt Dışı Doktora Sonrası Araştırma Burs Programı": "TÜBİTAK 2219 International Postdoctoral Research Fellowship Programme",
    "Erasmus Personel Hareketliliği": "Erasmus Staff Mobility",
    # fon kaynakları
    "TÜBİTAK 1002-C Doğal Afetler Odaklı Saha Çalışması Acil Destek Programı": "TÜBİTAK 1002-C Emergency Support Programme for Natural Disaster Field Studies",
    "Kütahya Dumlupınar Üniversitesi BAP": "Kütahya Dumlupınar University BAP", "İstanbul Teknik Üniversitesi BAP": "Istanbul Technical University BAP",
}


def cevir(h, ek):
    tablo = {**ek, **S}
    for a in sorted(tablo, key=len, reverse=True):
        h = h.replace(a, tablo[a])
    h = h.replace('href="/kisiler"', 'href="/en/people"')
    return h


def main():
    import yaml, html as H
    kisiler = {k["slug"]: k for k in yaml.safe_load((KOK / "_data/cv.yml").read_text(encoding="utf-8"))}
    ek = json.loads((KOK / "sitefinity/projeler_en.json").read_text(encoding="utf-8"))
    ek = {a + ".": b + "." for a, b in ek.items()} | ek
    for f in sorted((KOK / "sitefinity").glob("cv-*.html")):
        if f.stem.endswith("-en"):
            continue
        k = kisiler.get(f.stem[3:], {})
        ozel = dict(ek)
        if k.get("ozgecmis") and k.get("ozgecmis_en"):
            ozel[H.escape(k["ozgecmis"])] = H.escape(k["ozgecmis_en"])
        for a, b in zip(k.get("uzmanlik") or [], k.get("uzmanlik_en") or []):
            ozel[">" + H.escape(a) + "<"] = ">" + H.escape(b) + "<"
        (f.parent / (f.stem + "-en.html")).write_text(cevir(f.read_text(encoding="utf-8"), ozel), encoding="utf-8")
        print("yazıldı", f.stem + "-en.html")


if __name__ == "__main__":
    main()
