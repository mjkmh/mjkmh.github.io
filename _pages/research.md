---
title: "MJKMH - Projeler"
layout: textlay
sitemap: false
permalink: /projeler/
---

# Projeler

{% assign gruplar = "TÜBİTAK,Avrupa Birliği,BAP" | split: "," %}
{% assign yazilan = 0 %}
{% for g in gruplar %}
{% assign liste = site.data.projeler | where: "group", g %}
{% if liste.size > 0 %}
{% if yazilan > 0 %}<hr>{% endif %}
<h2 markdown="0" class="kisi-bolum">{{ g }} Projeleri</h2>
<ul markdown="0" class="projeler">
{% for p in liste %}
<li><strong>{% if p.url %}<a href="{{ p.url }}" target="_blank" rel="noopener">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}</strong><br><span class="son-kaynak">{{ p.funder }}{% if p.code %} · {{ p.code }}{% endif %}{% if p.start %} · {{ p.start }}{% if p.end %}–{{ p.end }}{% endif %}{% endif %}{% if p.status %} · <span class="proje-durum{% if p.status == 'Devam Ediyor' %} yuruyen{% endif %}">{{ p.status }}</span>{% endif %}{% if p.budget %} · Bütçe: {{ p.budget }}{% endif %}{% if p.team %}<br>Ekip: {{ p.team }}{% endif %}</span>{% if p.announcement %}<div class="proje-duyuru"><strong>Duyuru:</strong> {{ p.announcement }}</div>{% endif %}</li>
{% endfor %}
</ul>
{% assign yazilan = yazilan | plus: 1 %}
{% endif %}
{% endfor %}
{% if yazilan == 0 %}Henüz proje eklenmedi.{% endif %}
