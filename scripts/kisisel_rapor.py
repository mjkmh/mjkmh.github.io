"""Tek bir araştırmacının Scopus yayınlarını JSON olarak çıkarır (siteye yazmaz).
Kullanım: python scripts/kisisel_rapor.py <scopus_id> <ad> <cikti.json>"""
import json, sys, copy
from pathlib import Path
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parent))
import scopus_guncelle as sg

sid, ad, cikti = sys.argv[1], sys.argv[2], sys.argv[3]
ayar = yaml.safe_load(sg.AYAR.read_text(encoding="utf-8"))
ayar = copy.deepcopy(ayar); ayar["uyeler"] = [{"scopus_id": sid, "ad": ad}]; ayar["sadece_kurum"] = []
tekil = sg.api_ile_topla(ayar["uyeler"], False)
yillar = {str(y) for y in range(1950, 2100)}
g = sg.girdileri_kur(tekil, ayar, [], yillar)
sg.crossref_tarihleri(g)
Path(cikti).write_text(json.dumps({"ad": ad, "scopus_id": sid, "istatistik": sg.istatistik(g), "yayinlar": g},
                                  ensure_ascii=False, indent=1, default=str), encoding="utf-8")
print(len(g), "yayın yazıldı")
