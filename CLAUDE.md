# MJKMH Web Sitesi — Devir Notu (Claude için)

Bu dosya, mjkmh.itu.edu.tr sitesi üzerindeki çalışmaların başka bir Claude hesabında/oturumunda
kesintisiz sürdürülmesi için yazılmıştır (son güncelleme: 10.11.2026). Yeni oturumda önce bu dosyayı
baştan sona oku.

## 1. Kim, ne, nerede

- **Sahip / muhatap:** Doç. Dr. Enes Zengin (İTÜ Maden Fakültesi, Jeoloji Mühendisliği Bölümü).
  Siteyi o yönetir. **Her zaman Türkçe yaz** (İngilizce yanıt verildiğinde şikâyet etti).
- **Canlı site:** https://mjkmh.itu.edu.tr — Sitefinity CMS 12.2 (İTÜ BİDB barındırıyor).
  İngilizce sürüm: `/en/...`
- **Veri ve üretici betikler:** bu depo, `mjkmh/mjkmh.github.io` (GitHub). Ayrıca Jekyll ile
  https://mjkmh.github.io de yayımlanıyor, ama asıl site Sitefinity'dir.
- **Grup adı:** Mühendislik Jeolojisi – Kaya Mekaniği – Hidrojeoloji (MJKMH) Çalışma Grubu
  (EN: Engineering Geology – Rock Mechanics – Hydrogeology (EGRMH) Working Group).

## 2. Kesin kurallar (kullanıcının açık talimatları)

1. **Onay almadan işlem yapma** — özellikle silme, yayından kaldırma, e-posta/mesaj gönderme.
   Kullanıcının açıkça istediği işler için tekrar sormaya gerek yok.
2. **Şifre ya da API anahtarı asla yazma/girme.** Sitefinity'ye kullanıcı kendisi giriş yapar.
   Oturum düştüğünde (giriş sayfası açılırsa) kullanıcıdan "giriş yapın" iste. Kullanıcı şifresini
   vermeyi teklif ederse reddet ve paylaşmamasını söyle.
3. **CAPTCHA çözme.**
4. Mesaj/e-posta yalnızca kullanıcının açık onayıyla gönderilir.
5. Profil bağlantıları (Scopus, ORCID, Scholar, WoS, AVESİS vb.) **yalnızca doğrulanmış** olanlar.
6. **Öğrenci numaraları** gibi kişisel veriler herkese açık sayfalarda yer almaz.
7. Kişisel sayfalar (CV) **menüde gösterilmez**; Kişiler/People listesindeki isimlerden bağlanır.
8. Türkçe içeriklerin İngilizce sürümünde başlık İngilizceye çevrilir ve sonuna **"(in Turkish)"** eklenir.

## 3. Depo yapısı

| Yol | İçerik |
|---|---|
| `_data/yayinlar.yml` | Scopus'tan çekilen yayınlar (elle düzeltmeler korunur, bkz. `scripts/README.md`) |
| `_data/cv.yml` | 11 aktif üyenin CV verisi (slug, ad, unvan, eposta, foto, profiller, özgeçmiş TR/EN, eğitim, projeler, tezler, ödüller...) |
| `_data/projeler.yml` | Grup projeleri (title, funder, code, start/end, status, team) |
| `_data/aktif_uyeler.yml` | Ana sayfadaki "Araştırmacı" sayısı (şu an 11) |
| `scripts/scopus_ayarlar.yml` | Scopus ID'leri; emekli hocalar da dahil (geçmiş yayınlar için) |
| `scripts/scopus_guncelle.py` | Scopus → `yayinlar.yml` + `sitefinity/yayinlar.html` |
| `scripts/anasayfa_uret.py` | Ana sayfa içerik bloğu → `sitefinity/anasayfa.html` |
| `scripts/cv_uret.py`, `scripts/cv_en.py` | Kişisel sayfalar → `sitefinity/cv-<slug>.html` ve `cv-<slug>-en.html` |
| `scripts/lab_uret.py` | Laboratuvar sayfaları → `sitefinity/lab-*.html` |
| `scripts/kisisel_rapor.py` | Kişi bazlı Scopus raporu (workflow `kisisel_rapor.yml`) |
| `sitefinity/en_yardimci.js` | Sitefinity düzenleme ekranında içerik doldurma yardımcıları |
| `sitefinity/ceviri.js` | TR→EN çeviri sözlüğü ve `__cevir(html)` |
| `sitefinity/projeler_en.json`, `tr_basliklar_en.json` | Proje / Türkçe yayın başlıklarının İngilizceleri |

Sitefinity `<style>` bloklarını sildiği için **tüm stiller satır içi** (inline) yazılır.

## 4. Otomasyon (GitHub Actions)

- `.github/workflows/scopus.yml`: her ayın 1'inde 07:17'de çalışır (elle de tetiklenebilir).
  Scopus'u çeker, `anasayfa_uret.py`'yi çalıştırır, değişiklik varsa commit eder.
  Gizli değişken: `SCOPUS_API_KEY` (ve isteğe bağlı `SCOPUS_INSTTOKEN`).
- **Önemli:** Workflow yalnızca depodaki HTML'leri günceller. **Sitefinity'ye kendiliğinden geçmez.**
  Güncel HTML'i Sitefinity'ye aktarmak için Bölüm 6'daki yöntem kullanılır.
- Tetikleme (GraphQL kapalı olduğundan REST):
  `gh api -X POST repos/mjkmh/mjkmh.github.io/actions/workflows/scopus.yml/dispatches -f ref=main`
- `kisisel_rapor.yml` çıktıyı gzip+base64 JSON olarak log'a basar (artifact indirme engelli olduğu için).

### Q / yüzdelik kuralı (kullanıcı kararı, 10.11.2026)
Her makale için **makalenin yayın yılına ait CiteScore**, derginin kategorileri arasındaki
**en yüksek yüzdelik** kullanılır. O yılın değeri henüz yoksa (ör. 2026 makalesi, en güncel 2025)
yayın yılından önceki en yakın yıl alınır; sonraki aylık güncellemelerde ilgili yılın değeri gelince
otomatik ona geçer. `top_percent = 100 - yüzdelik`.
Açık soru: GSA makalesi (Zengin 2026, Remote Sensing in Earth Systems Sciences) sitede "Q1 (%18)"
görünüyor, kullanıcı %28 bekliyor. Kullanıcıdan Scopus'ta hangi kategori/yılı gördüğü soruldu.

## 5. Sitefinity sayfa haritası

| TR | EN | Not |
|---|---|---|
| `/` (düzenleme: `/anasayfa/Action/Edit/tr`) | `/en` (düzenleme: `/home/Action/Edit/en`) | Tek içerik bloğu = `anasayfa.html` (EN: `__cevir` ile) |
| `/hakkimizda` | `/en/about-us` | MVC blok. Sonda "Emekli Öğretim Üyelerimiz" listesi (sadece isim) |
| `/kisiler` | `/en/people` | MVC blok. 11 isim kişisel sayfalara bağlı |
| `/kisiler/<slug>` | `/en/people/<slug>` (düzenleme: `/people/<slug>/Action/Edit/en`) | Menüde yok |
| `/laboratuvar` + 3 alt sayfa | `/en/laboratories` + 3 alt sayfa | "Örnek içerik" uyarısı kaldırıldı |
| `/yayinlar` | `/en/publications` | `yayinlar.html` |
| `/projeler` | `/en/projects` | Devam Eden / Tamamlanan → alt başlıklar TÜBİTAK, TTO ve Sanayi/Kamu İşbirliği, BAP, Uluslararası |
| `/haberler`, `/haber-detay/...` | `/en/news` | 3 "[Örnek]" haber; kullanıcı kalsın dedi |
| `/etkinlikler` | `/en/events` | Takvim + Events widget'ı; 3 "[Örnek]" etkinlik |
| `/iletisim` | `/en/contact` | EN'de iletişim formu yok |

11 aktif üye (slug): enes-zengin, irfan-yolcubal, yilmaz-mahmutoglu, omer-undul, ozge-dinc-gogus,
erkan-bozkurtoglu, kayhan-develi, mehmet-korkut, gokhan-sans, dilek-karapinar, mehmet-mert-dogu.

Emekliler (Hakkımızda sonunda, sadece isim): Prof. Dr. Remzi Karagüzel, Prof. Dr. Enver Vural Yavuz,
Prof. Dr. Mustafa Erdoğan, Prof. Dr. Turgut Öztaş. Vardar (vefat) ve Yüzer "Hocalarımız" bölümünde
oldukları için bu listede yok. Scopus'ta Erdoğan ve Öztaş için profil bulunamadı.

## 6. Sitefinity'de içerik güncelleme yöntemi (tarayıcı paneli + JavaScript)

Kullanıcı Sitefinity'ye giriş yapmış olmalı. Düzenleme adresi:
TR `https://mjkmh.itu.edu.tr/<slug>/Action/Edit/tr`, EN `https://mjkmh.itu.edu.tr/<enslug>/Action/Edit/en`.

Düzenleme sayfasında:
```js
await new Promise(r=>setTimeout(r,2500));
eval(await fetch('https://raw.githubusercontent.com/mjkmh/mjkmh.github.io/main/sitefinity/en_yardimci.js?'+Date.now()).then(r=>r.text()));
const h = await fetch('https://raw.githubusercontent.com/mjkmh/mjkmh.github.io/<COMMIT>/sitefinity/<dosya>.html').then(r=>r.text());
const ds = __docks(/^Content blockEditMore/);           // içerik blokları
const i  = ds.findIndex(d => /ayırt edici metin/.test(d.textContent));
const x  = await __legacyFill(h, i);                    // ['legacy'|'mvc', uzunluk, ...]
await new Promise(r=>setTimeout(r,2500));
if (x[0]=='mvc') { [...document.querySelectorAll('button')].find(b=>b.offsetParent&&b.textContent.trim()=='Save').click(); await new Promise(r=>setTimeout(r,3000)); }
[...document.querySelectorAll('a')].find(a=>a.offsetParent&&a.textContent.trim().startsWith('Publish')).click();
```
- **raw.githubusercontent önbelleği:** `main` yerine commit hash'i kullan; yoksa eski dosya gelebilir.
- **Legacy (RadEditor) bloklar** kendiliğinden kaydolur → doğrudan Publish.
  **MVC (kendo) bloklar** (Kişiler, Hakkımızda, About Us) için **önce "Save", sonra Publish**;
  Save'siz Publish değişikliği kaybeder.
- Publish sayfadan çıkar; script "navigated" hatası verir — normaldir. Ardından herkese açık
  sayfayı `fetch` ile çekip doğrula. Herkese açık sayfa bazen "Sitefinity trial version" ara sayfası
  döndürür (kısa yanıt) → birkaç kez yeniden dene.
- İngilizce içerik: `ceviri.js` yüklenip `__cevir(trHtml)`; `window.__eksik` çevrilmemiş metinleri listeler.
  Yeni terimleri `ceviri.js` sözlüğüne ekle.
- Yeni sayfa: mevcut bir sayfayı "Duplicate" et, üst sayfa seç, "Show in navigation" işaretini kaldır,
  URL'yi "Change" ile değiştir, "Create and return to Pages". EN çevirisi: Pages?lang=en → satırdaki EN
  "Add" → ad/URL → düzenlemede "Copy from another language", "Keep all language versions synced"
  işaretini kaldır.
- Sayfa başlığı (tarayıcı sekmesi): Pages listesinde satır → Actions → "Title & Properties" →
  "Title for search engines".
- Görsel değiştirme (referansları bozmadan): Content → Images → kütüphane → görsel → "Replace the file";
  dosya `DataTransfer` ile `input[type=file]`'a verilip Publish. Wikimedia Commons'tan alınırsa
  lisans/yazar kredisini sayfada güncelle.
- Etkinlik: Content → Events → "Create an event". Kart şablonu **görsel bekler**; görsel yoksa kart
  boş ve çok uzun görünür → "Related media" → "Select image" ile mutlaka görsel ekle.
- Tarayıcı paneli gizliyken ekran görüntüsü ve sürükle-bırak çalışmaz; widget sürüklemek için
  kullanıcıdan pencereyi önde tutmasını iste.
- Silinen sayfalar geri dönüşüm kutusuna gider (geri alınabilir).

## 7. Yapılanlar (özet)

- Kişisel sayfalar: 11 kişi × TR/EN, ortak şablon ve renkli etiket sistemi (rol, devam/tamamlandı,
  format). Yalnızca sayfa sahibinin adı vurgulanır. Telefonda fotoğraf ismin üstüne geçer.
- Ana sayfa: tanıtım, otomatik sayaçlar (Makale, İlk %10, Q1, Devam Eden Proje, Araştırmacı),
  Haberler ve Duyurular, Son Yayınlar (5), Son Bildiriler (5, Scopus + CV), Son Projeler (5),
  Çalışma Alanlarımız (en altta). İçerik 1110 px'te ortalı. Mühendislik Jeolojisi görseli:
  Brienz heyelanı (Clemenspool, CC0).
- Yayınlar: Scopus, tüm MJKMH üyeleri vurgulu, Q/yüzdelik etiketleri.
- Projeler: gruplandı (bkz. Bölüm 5). İTÜ1773 "Düzensiz Basamaklı..." projesi: Yürütücü Ömer Ündül;
  Araştırmacılar Enes Zengin, Mehmet Korkut, Mehmet Mert Doğu. TÜBİTAK 1001 126M496 tam ekip.
- Hizmetler/Services sayfası silindi (geri dönüşüm kutusunda).
- Laboratuvar sayfalarındaki "Örnek içerik" uyarısı kaldırıldı (`lab_uret.py`'de de boş).
- Etkinlikler: takvim eklendi, genel İTÜ etkinlik kutusu kaldırıldı, 3 örnek etkinlik görselli.
- Arazi haberi görseli: Berlin Leipziger Platz kazı çukuru (Fridolin freudenfett, CC BY-SA 4.0).
- `MJKMH_Bilgi_Toplama.xlsx`: öğretim üyelerinden bilgi toplamak için Excel formu (hazır, henüz gönderilmedi).

## 8. Bekleyen işler / açık sorular

1. GSA makalesi yüzdeliği (%18 vs %28) — kullanıcının cevabı bekleniyor (Bölüm 4).
2. Etkinlikler sayfasındaki işe yaramayan "Arşiv" kutusunun kaldırılması (kullanıcıya soruldu).
3. İngilizce Events sayfasını TR ile aynı düzene getirmek (takvim + görselli kartlar).
4. Takvimdeki gün/ay adları İngilizce görünüyor (Sitefinity dil ayarı).
5. İstJeo-7 örnek etkinliğinin tarihi uydurma (20–21 Mayıs 2027); gerçek tarih gelince düzelt.
6. Laboratuvar sayfalarındaki "eklenecek" alanlar ve fotoğraf yer tutucuları — gizlensin mi? (soruldu)
7. İngilizce İletişim sayfasına form eklenmesi.
8. BİDB'ye gidecek e-postaya "Sitefinity trial version" ara sayfası sorunu eklenecek
   (ziyaretçilere de görünüyor). E-posta kullanıcı onayı olmadan gönderilmez.
9. Excel bilgi toplama formunun öğretim üyelerine gönderilmesi; "Başlık (İngilizce)" sütunu eklenmesi önerildi.
10. Ana sayfaya "Yaklaşan Etkinlikler" kısa listesi eklenmesi teklif edildi.

## 9. Ana sayfayı / CV'leri yeniden üretip yayımlama (tipik akış)

```bash
python scripts/anasayfa_uret.py          # ana sayfa
python scripts/cv_uret.py && python scripts/cv_en.py   # kişisel sayfalar
git add -A && git commit -m "..." && git push
```
Sonra Bölüm 6'daki yöntemle ilgili Sitefinity sayfalarına commit hash'i ile aktar ve herkese açık
sayfayı doğrula.
