---
title: "MJKMH - Projeler"
layout: textlay
sitemap: false
permalink: /projeler/
---

# Projeler

{% if site.data.projeler.size > 0 %}
{% for p in site.data.projeler %}
<div markdown="0" class="proje-kart">
{% if p.status %}<span class="proje-rozet{% if p.status == 'Devam Ediyor' %} devam{% endif %}">{{ p.status }}</span>{% endif %}
<table class="proje-tablo">
<tr><th>Proje Adı:</th><td><strong>{% if p.url %}<a href="{{ p.url }}" target="_blank" rel="noopener">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}</strong></td></tr>
<tr><th>Destekleyen Kuruluş:</th><td>{{ p.funder | default: "—" }}{% if p.code %} ({{ p.code }}){% endif %}</td></tr>
<tr><th>Proje Bütçesi:</th><td>{{ p.budget | default: "—" }}</td></tr>
<tr><th>Başlangıç Tarihi:</th><td>{{ p.start | default: "—" }}</td></tr>
<tr><th>Bitiş Tarihi:</th><td>{{ p.end | default: "—" }}</td></tr>
<tr><th>Ekip:</th><td>{{ p.team | default: "—" }}</td></tr>
</table>
{% if p.announcement %}<div class="proje-duyuru"><strong>Duyuru:</strong> {{ p.announcement }}</div>{% endif %}
</div>
{% endfor %}
{% else %}
Henüz proje eklenmedi.
{% endif %}
