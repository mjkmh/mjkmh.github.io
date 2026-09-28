---
title: "MJKMH - Projeler"
layout: textlay
sitemap: false
permalink: /projeler/
---

# Projeler

{% if site.data.projeler.size > 0 %}
<ul markdown="0" class="projeler">
{% for p in site.data.projeler %}
<li><strong>{% if p.url %}<a href="{{ p.url }}" target="_blank" rel="noopener">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}</strong><br><span class="son-kaynak">{{ p.funder }}{% if p.code %} · {{ p.code }}{% endif %}{% if p.start %} · {{ p.start }}{% if p.end %}–{{ p.end }}{% endif %}{% endif %}{% if p.status %} · <span class="proje-durum{% if p.status == 'Yürüyen' %} yuruyen{% endif %}">{{ p.status }}</span>{% endif %}{% if p.people %}<br>{{ p.people }}{% endif %}</span></li>
{% endfor %}
</ul>
{% else %}
Henüz proje eklenmedi.
{% endif %}
