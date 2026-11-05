# Yayın listesini Scopus'tan güncelleme

**Otomatik:** `.github/workflows/scopus.yml` her ayın 1'inde GitHub'da çalışır; yeni yayın varsa
`_data/yayinlar.yml` güncellenir ve site kendiliğinden yenilenir. Sitefinity için üretilen HTML
https://mjkmh.github.io/sitefinity/yayinlar.html adresinde yayımlanır.
GitHub → Actions → "Scopus yayın güncellemesi" → "Run workflow" ile istenildiği an çalıştırılabilir.
Gerekli gizli değişken: `SCOPUS_API_KEY` (isteğe bağlı: `SCOPUS_INSTTOKEN`).

Aşağıdaki adımlar betiği kendi bilgisayarınızda çalıştırmak içindir.

`scopus_guncelle.py`, grup üyelerinin Scopus yayınlarını çeker ve iki çıktı üretir:

- `_data/yayinlar.yml` → GitHub sitesindeki Yayınlar sayfası
- `sitefinity/yayinlar.html` → mjkmh.itu.edu.tr Yayınlar sayfasına yapıştırılacak HTML

## İlk kurulum (bir kez)

```
pip install pybliometrics pandas pyyaml openpyxl
```

API anahtarı, `Scopus.ipynb` için daha önce yaptığınız `pybliometrics.init()` kurulumundan okunur. Anahtar bu depoya yazılmaz.

## Her güncellemede

İTÜ ağındayken ya da VPN açıkken, depo klasöründe:

```
python scripts/scopus_guncelle.py --crossref
git add _data/yayinlar.yml sitefinity
git commit -m "Yayınlar güncellendi"
git push
```

Betik sonunda kaç yeni yayın geldiğini listeler. GitHub sitesi birkaç dakika içinde kendiliğinden güncellenir. `sitefinity/yayinlar.html` dosyasının içeriği Sitefinity'de Yayınlar sayfasındaki içerik bloğuna HTML olarak yapıştırılır.

## Ayarlar — `scopus_ayarlar.yml`

- `uyeler`: Scopus ID'si ve sitede görünecek kısa ad. Yeni üye eklemek ya da çıkarmak için burayı düzenleyin.
- `haric_turler`: listeye alınmayacak yayın türleri (varsayılan: Erratum).
- `haric_yayinlar`: listeye hiç alınmaması gereken tek tek yayınlar (EID veya DOI).

## Elle düzeltmeler korunur

`_data/yayinlar.yml` içinde elle değiştirilen `year`, `date`, `title`, `image`, `image_credit` ve `abstract` alanları sonraki çalıştırmalarda korunur. Scopus'ta bulunmayan ama listede kalması gereken bir yayına `manuel: true` eklenmelidir.

API'ye erişilemezse notebook'un Excel dışa aktarımıyla da çalışır:

```
python scripts/scopus_guncelle.py --excel exports/Scopus_Yayin_Listesi_....xlsx
```
