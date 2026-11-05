---
title: "MJKMH - Yayınlar"
layout: gridlay
sitemap: false
permalink: /yayinlar/
---

# Yayınlar

<p class="yayin-not">Grup üyeleri <span class="uye">koyu kırmızı</span> ile gösterilmiştir.</p>

{% assign yillar = site.data.yayinlar | group_by: "year" %}
{% for yil in yillar %}
{% unless forloop.first %}<hr>{% endunless %}
<h2 class="kisi-bolum yayin-yil">{{ yil.name }}</h2>
{% assign yil_metin = yil.name | append: "" %}
{% if site.yayin_detayli_yillar contains yil_metin %}
{% for y in yil.items %}
<div class="row yayin-detay" markdown="0">
<div class="col-sm-4">
<img src="{{ site.url }}{{ site.baseurl }}/images/{% if y.image %}yayinlar/{{ y.image }}{% else %}kisiler/fotograf-yok.png{% endif %}" class="img-responsive yayin-resim" alt="" />
{% if y.image_credit %}<p class="gorsel-kaynak">Görsel: {{ y.image_credit }}</p>{% endif %}
</div>
<div class="col-sm-8">
<p class="yayin-baslik"><strong>{{ y.title }}</strong></p>
<p class="yazarlar">{% include yazarlar.html authors=y.authors %}</p>
<p><em>{{ y.source }}{% if y.source_detail %}, {{ y.source_detail }}{% endif %}</em>{% if y.doi %} · <a href="https://doi.org/{{ y.doi }}" target="_blank" rel="noopener">doi:{{ y.doi }}</a>{% endif %} <span class="etiket">{{ y.type }}</span>{% if y.quartile or y.top_percent %}{% assign q = y.quartile | slice: 1, 2 %} <span class="etiket q">{{ q }}{% if y.top_percent %} (%{{ y.top_percent }}){% endif %}</span>{% endif %}</p>
{% if y.abstract %}<div class="ozet kisa">{{ y.abstract }}</div>
<a href="#" class="devami" onclick="var o=this.previousElementSibling;o.classList.toggle('kisa');this.textContent=o.classList.contains('kisa')?'devamı':'kapat';return false;">devamı</a>{% endif %}
</div>
</div>
{% endfor %}
{% else %}
<ul class="yayinlar">
{% for y in yil.items %}
<li>
<strong>{{ y.title }}</strong><br>
<span class="yazarlar">{% include yazarlar.html authors=y.authors %}</span><br>
<em>{{ y.source }}{% if y.source_detail %}, {{ y.source_detail }}{% endif %}</em>{% if y.doi %} · <a href="https://doi.org/{{ y.doi }}" target="_blank" rel="noopener">doi:{{ y.doi }}</a>{% endif %} <span class="etiket">{{ y.type }}</span>{% if y.quartile or y.top_percent %}{% assign q = y.quartile | slice: 1, 2 %} <span class="etiket q">{{ q }}{% if y.top_percent %} (%{{ y.top_percent }}){% endif %}</span>{% endif %}
</li>
{% endfor %}
</ul>
{% endif %}
{% endfor %}
