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
    return (f'<table style="width:100%;border-collapse:collapse;border:0;"><tbody><tr>'
            f'<td style="width:170px;vertical-align:top;padding:0 24px 0 0;">'
            f'<img src="{e(k["foto"])}" alt="{e(k["ad"])}" width="160" height="160" style="width:160px;height:160px;display:block;" /></td>'
            f'<td style="vertical-align:top;">'
            f'<p style="margin:0;font-size:14px;color:#777;">{e(k["unvan"])}</p>'
            f'<p style="margin:0 0 8px 0;font-size:28px;font-weight:bold;color:{LAC};line-height:1.2;">{e(k["ad"])}</p>'
            f'<p style="margin:0 0 4px 0;font-size:14px;color:#555;">İTÜ Maden Fakültesi, Jeoloji Mühendisliği Bölümü</p>'
            f'<p style="margin:0 0 12px 0;font-size:14px;"><a href="mailto:{e(k["eposta"])}">{e(k["eposta"])}</a></p>'
            f'<p style="margin:0;">{ikon}</p></td></tr></tbody></table>')


def kutular(say):
    k = [(say["makale"], "Makale"), (say["ilk10"], "İlk %10’luk Dilimdeki Makale"), (say["Q1"], "Q1 Makale")]
    return '<div style="margin:22px 0 0 0;">' + "".join(
        f'<div style="display:inline-block;vertical-align:top;min-width:150px;margin:0 12px 10px 0;padding:12px 16px;'
        f'background:#f6f8fb;border-top:3px solid {LAC};"><span style="display:block;font-size:30px;font-weight:bold;'
        f'color:{LAC};line-height:1.1;">{n}</span><span style="display:block;font-size:13px;color:#555;margin-top:4px;">{e(t)}</span></div>'
        for n, t in k) + '</div>'


def yayin_li(g):
    yz = ", ".join(f'<strong style="{UYE}">{e(a["n"])}</strong>' if a.get("m") else e(a["n"]) for a in g.get("authors") or [])
    kaynak = e(g.get("source") or "") + (f", {e(g['source_detail'])}" if g.get("source_detail") else "")
    s = f'<li style="margin:0 0 10px 0;line-height:1.55;">{yz} ({g.get("year")}). {e(g.get("title") or "")}. <em>{kaynak}</em>.'
    if g.get("doi"):
        s += f' <a href="https://doi.org/{e(g["doi"])}" target="_blank">DOI</a>'
    if g.get("type"):
        s += " " + etiket(g["type"], TUR_RENK.get(g["type"], ("#f1f1f1", "#555")))
    q = re.search(r"Q[1-4]", g.get("quartile") or "")
    if q:
        s += " " + etiket(q.group(0) + (f" (%{g['top_percent']})" if g.get("top_percent") else ""), Q_RENK[q.group(0)])
    return s + "</li>"


def satirlar(liste):
    return ('<table style="width:100%;border-collapse:collapse;font-size:15px;"><tbody>' + "".join(
        f'<tr><td style="width:150px;padding:6px 12px 6px 0;color:#777;vertical-align:top;">{e(a)}</td>'
        f'<td style="padding:6px 0;vertical-align:top;">{b}</td></tr>' for a, b in liste) + '</tbody></table>')


def sayfa(k, yayinlar, projeler, logolar):
    benim = [g for g in yayinlar if any(a.get("m") and a.get("n") == k["yazar_adi"] for a in g.get("authors") or [])]
    p = [ust(k, logolar), kutular(istatistik(benim))]
    if k.get("ozgecmis"):
        p += [baslik("Özgeçmiş"), f'<p style="font-size:16px;line-height:1.7;text-align:justify;">{e(k["ozgecmis"])}</p>']
    if k.get("uzmanlik"):
        p += [baslik("Uzmanlık Alanları"), '<p>' + "".join(
            f'<span style="display:inline-block;margin:0 6px 6px 0;padding:3px 12px;border-radius:14px;background:#eef2f7;color:{LAC};font-size:14px;">{e(u)}</span>'
            for u in k["uzmanlik"]) + '</p>']
    p += [baslik("Eğitim"), satirlar([(a, e(b)) for a, b in k["egitim"]])]
    if k.get("gorevler"):
        p += [baslik("Görevler ve Ödüller"), satirlar([(c, f"{e(a)}: {e(b)}") for a, b, c in k["gorevler"]])]
    pr = [x for x in projeler if k["ad"] in str(x.get("team") or "")]
    if pr:
        p.append(baslik("Projeler", len(pr)))
        for x in pr:
            rol = re.search(re.escape(k["ad"]) + r"\s*\(([^)]+)\)", str(x["team"]))
            tarih = " – ".join(dict.fromkeys(t[-4:] for t in [str(x.get("start") or ""), str(x.get("end") or "")] if t))
            p.append(f'<div style="border-left:4px solid {LAC};background:#fafafa;padding:10px 16px;margin:0 0 10px 0;">'
                     f'<p style="margin:0 0 4px 0;font-size:13px;color:#666;">{e(x.get("funder") or "")}'
                     f'{" · " + e(x["code"]) if x.get("code") else ""}{" · " + tarih if tarih else ""}'
                     f'{" · " + e(rol.group(1)) if rol else ""} · {e(x.get("status") or "")}</p>'
                     f'<p style="margin:0;font-size:15px;line-height:1.4;"><strong>{e(x["title"])}</strong></p></div>')
    p.append(baslik("Yayınlar", len(benim)))
    p.append('<p style="margin:-6px 0 14px 0;font-size:12px;color:#888;">Scopus’tan otomatik olarak alınmaktadır. '
             'Q değerleri derginin güncel Scopus CiteScore dilimine göredir.</p>')
    yil = None
    for g in benim:
        if g.get("year") != yil:
            if yil is not None:
                p.append("</ol>")
            yil = g.get("year")
            p.append(f'<h4 style="margin:18px 0 8px 0;color:#444;">{yil}</h4><ol style="padding-left:22px;margin:0;">')
        p.append(yayin_li(g))
    if yil is not None:
        p.append("</ol>")
    og = k.get("ogrenciler") or {}
    if k.get("tezler") or og:
        p.append(baslik("Danışmanlık"))
        if og.get("devam"):
            p.append(f'<p style="margin:0 0 6px 0;"><strong>Devam eden lisans öğrencileri:</strong> {e(", ".join(og["devam"]))}</p>')
        if og.get("mezun"):
            p.append(f'<p style="margin:0 0 6px 0;"><strong>Mezun lisans öğrencileri:</strong> {e(", ".join(og["mezun"]))}</p>')
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
