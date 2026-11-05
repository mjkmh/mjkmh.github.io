---
title: "MJKMH - Yayınlar"
layout: gridlay
sitemap: false
permalink: /yayinlar/
---

# Yayınlar

<p class="yayin-not">Grup üyeleri <span class="uye">koyu kırmızı</span> ile gösterilmiştir.</p>

{% assign st = site.data.yayin_istatistik %}
<div class="yayin-istatistik">
<div class="kutu makale"><b>{{ st.makale }}</b>Makale</div>
<div class="kutu ilk10"><b>{{ st.ilk10 }}</b>İlk %10</div>
<div class="kutu q1"><b>{{ st.Q1 }}</b>Q1</div>
<div class="kutu q2"><b>{{ st.Q2 }}</b>Q2</div>
<div class="kutu q3"><b>{{ st.Q3 }}</b>Q3</div>
<div class="kutu q4"><b>{{ st.Q4 }}</b>Q4</div>
<div class="kutu bildiri"><b>{{ st.bildiri }}</b>Bildiri</div>
</div>
<p class="yayin-not">Q değerleri Scopus CiteScore yüzdeliklerine göredir. Q değeri bulunmayan makaleler ve derlemeler sayılara katılmamıştır.</p>

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
<p><em>{{ y.source }}{% if y.source_detail %}, {{ y.source_detail }}{% endif %}</em>{% if y.doi %} · <a href="https://doi.org/{{ y.doi }}" target="_blank" rel="noopener">doi:{{ y.doi }}</a>{% endif %} <span class="etiket{% if y.type == 'Bildiri' %} bildiri{% endif %}">{{ y.type }}</span>{% if y.quartile or y.top_percent %}{% assign q = y.quartile | slice: 1, 2 %} <span class="etiket {{ q | downcase }}">{{ q }}{% if y.top_percent %} (%{{ y.top_percent }}){% endif %}</span>{% endif %}</p>
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
<em>{{ y.source }}{% if y.source_detail %}, {{ y.source_detail }}{% endif %}</em>{% if y.doi %} · <a href="https://doi.org/{{ y.doi }}" target="_blank" rel="noopener">doi:{{ y.doi }}</a>{% endif %} <span class="etiket{% if y.type == 'Bildiri' %} bildiri{% endif %}">{{ y.type }}</span>{% if y.quartile or y.top_percent %}{% assign q = y.quartile | slice: 1, 2 %} <span class="etiket {{ q | downcase }}">{{ q }}{% if y.top_percent %} (%{{ y.top_percent }}){% endif %}</span>{% endif %}
</li>
{% endfor %}
</ul>
{% endif %}
{% endfor %}
