---
title: "MJKMH - Ana Sayfa"
layout: homelay
sitemap: false
permalink: /
---

[İstanbul Teknik Üniversitesi](https://www.itu.edu.tr) [Maden Fakültesi](https://mines.itu.edu.tr) [Jeoloji Mühendisliği Bölümü](https://jeoloji.itu.edu.tr)’nde **Mühendislik Jeolojisi**, **Kaya Mekaniği** ve **Hidrojeoloji** (MJKMH) alanlarında çalışan bir araştırma grubuyuz.

{% if site.data.slider.size > 0 %}
<div markdown="0" id="carousel" class="carousel slide" data-ride="carousel" data-interval="5000" data-pause="hover">
<ol class="carousel-indicators">
{% for s in site.data.slider %}<li data-target="#carousel" data-slide-to="{{ forloop.index0 }}"{% if forloop.first %} class="active"{% endif %}></li>{% endfor %}
</ol>
<div class="carousel-inner">
{% for s in site.data.slider %}
<div class="item{% if forloop.first %} active{% endif %}">
<img src="{{ site.url }}{{ site.baseurl }}/images/slider/{{ s.image }}" alt="{{ s.caption }}" />
{% if s.caption %}<div class="carousel-caption">{{ s.caption }}</div>{% endif %}
</div>
{% endfor %}
</div>
<a class="left carousel-control" href="#carousel" role="button" data-slide="prev"><span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span><span class="sr-only">Önceki</span></a>
<a class="right carousel-control" href="#carousel" role="button" data-slide="next"><span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span><span class="sr-only">Sonraki</span></a>
</div>
{% endif %}

<div markdown="0" class="anasayfa-bolum">
<h2 class="bolum-baslik">Araştırma Alanları</h2>
<div class="row">
{% for a in site.data.arastirma_alanlari %}{% include kart.html name=a.name text=a.text image=a.image %}{% endfor %}
</div>
</div>

{% assign yayin_sayisi = site.data.yayinlar | size %}
{% assign q1_sayisi = site.data.yayinlar | where: "quartile", "(Q1 - Scopus)" | size %}
{% assign uye_sayisi = site.data.team_members | size %}
{% assign mezun_sayisi = site.data.mezunlar.doktora.size | plus: site.data.mezunlar.yuksek_lisans.size | plus: site.data.mezunlar.lisans.size %}
<div markdown="0" class="anasayfa-bolum rakamlar">
<div class="row">
<div class="col-xs-6 col-sm-3 rakam"><span class="sayi">{{ uye_sayisi }}</span><span class="etiket">Grup üyesi</span></div>
<div class="col-xs-6 col-sm-3 rakam"><span class="sayi">{{ yayin_sayisi }}</span><span class="etiket">Scopus yayını</span></div>
<div class="col-xs-6 col-sm-3 rakam"><span class="sayi">{{ q1_sayisi }}</span><span class="etiket">Q1 yayın</span></div>
<div class="col-xs-6 col-sm-3 rakam"><span class="sayi">{{ mezun_sayisi }}</span><span class="etiket">Mezun</span></div>
</div>
</div>

<div markdown="0" class="anasayfa-bolum">
<h2 class="bolum-baslik">Son Yayınlar <a class="bolum-link" href="{{ site.url }}{{ site.baseurl }}/yayinlar/">Tüm yayınlar</a></h2>
<div class="row">
{% for y in site.data.yayinlar limit: 3 %}
<div class="col-sm-4 kart">
<a href="{% if y.doi %}https://doi.org/{{ y.doi }}{% else %}{{ site.url }}{{ site.baseurl }}/yayinlar/{% endif %}"{% if y.doi %} target="_blank" rel="noopener"{% endif %}><img src="{{ site.url }}{{ site.baseurl }}/images/{% if y.image %}yayinlar/{{ y.image }}{% else %}kisiler/fotograf-yok.png{% endif %}" class="kart-resim" alt="" /></a>
<p class="kart-yayin-baslik">{{ y.title }}</p>
<p class="yazarlar">{% include yazarlar.html authors=y.authors %}</p>
<p class="kart-kaynak"><em>{{ y.source }}</em>, {{ y.year }}</p>
</div>
{% endfor %}
</div>
</div>

<div markdown="0" class="anasayfa-bolum">
<h2 class="bolum-baslik">Laboratuvarlar</h2>
<div class="row">
{% for l in site.data.laboratuvarlar %}{% include kart.html name=l.name text=l.text image=l.image %}{% endfor %}
</div>
</div>

{% if site.data.projeler.size > 0 %}
<div markdown="0" class="anasayfa-bolum">
<h2 class="bolum-baslik">Projeler</h2>
<ul class="projeler">
{% for p in site.data.projeler %}
<li><strong>{{ p.title }}</strong><br><span class="danisman">{{ p.funder }}{% if p.years %} · {{ p.years }}{% endif %}{% if p.role %} · {{ p.role }}{% endif %}{% if p.people %} · {{ p.people }}{% endif %}</span></li>
{% endfor %}
</ul>
</div>
{% endif %}
