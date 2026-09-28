---
title: "MJKMH - Ana Sayfa"
layout: homelay
sitemap: false
permalink: /
---

[İstanbul Teknik Üniversitesi](https://www.itu.edu.tr) [Maden Fakültesi](https://mines.itu.edu.tr) [Jeoloji Mühendisliği Bölümü](https://jeoloji.itu.edu.tr)’nde **Mühendislik Jeolojisi**, **Kaya Mekaniği** ve **Hidrojeoloji** (MJKMH) alanlarında çalışan bir araştırma grubuyuz.

<div markdown="0" id="carousel" class="carousel slide" data-ride="carousel" data-interval="4000" data-pause="hover" >
    <!-- Menu -->
    <ol class="carousel-indicators">
        <li data-target="#carousel" data-slide-to="0" class="active"></li>
        <li data-target="#carousel" data-slide-to="1"></li>
        <li data-target="#carousel" data-slide-to="2"></li>
        <li data-target="#carousel" data-slide-to="3"></li>
        <li data-target="#carousel" data-slide-to="4"></li>
        <li data-target="#carousel" data-slide-to="5"></li>
        <li data-target="#carousel" data-slide-to="6"></li>
    </ol>

    <!-- Items -->
    <div class="carousel-inner" markdown="0">
        <div class="item active">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/QPI_Rh.jpg" alt="Slide 1" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/SmartTipSide.jpg" alt="Slide 2" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/SaphireSTM2.jpg" alt="Slide 3" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/lab.jpg" alt="Slide 4" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/Fig_Science_Web.jpg" alt="Slide 5" />
        </div>       
         <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/BSCCO2gap2.jpg" alt="Slide 6" />
        </div>
    </div>
  <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Önceki</span>
  </a>
  <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Sonraki</span>
  </a>
</div>


Şu anda cihazlarımızı Münih'in tam merkezinde, Sommerfeld ve Röntgen'in çalıştığı *Sommerfeldkeller*’de kuruyoruz. Kuantum fiziği, soğuk atom çok cisim fiziği ve iki boyutlu kuantum malzemeler alanlarında çalışan dünya çapındaki gruplarla fikir alışverişinde bulunacağız. Ayrıca [SuperC konsorsiyumunun](https://superc2033.com/our-team/) gururlu bir üyesiyiz.

**Ekibimize katılacak tutkulu yeni doktora öğrencileri, doktora sonrası araştırmacılar ve yüksek lisans öğrencileri arıyoruz** [(ayrıntılar)]({{ site.url }}{{ site.baseurl }}/acik-pozisyonlar/) **!**





{% assign makaleler = site.data.yayinlar | where_exp: "y", "y.type != 'Bildiri'" %}
{% assign bildiriler = site.data.yayinlar | where: "type", "Bildiri" %}
<div markdown="0" class="row son-uclu">
<div class="col-md-4">
<h4>Son Yayınlar</h4>
<ul>{% include son_liste.html items=makaleler %}</ul>
<p class="son-tumu"><a href="{{ site.url }}{{ site.baseurl }}/yayinlar/">Tüm yayınlar</a></p>
</div>
<div class="col-md-4">
<h4>Son Bildiriler</h4>
<ul>{% include son_liste.html items=bildiriler %}</ul>
</div>
<div class="col-md-4">
<h4>Son Projeler</h4>
{% if site.data.projeler.size > 0 %}<ul>{% for p in site.data.projeler limit: 3 %}<li>{% if p.url %}<a href="{{ p.url }}" target="_blank" rel="noopener">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}<br><span class="son-kaynak">{{ p.funder }}{% if p.years %}, {{ p.years }}{% endif %}</span></li>{% endfor %}</ul>{% else %}<p class="son-kaynak">Henüz proje eklenmedi.</p>{% endif %}
</div>
</div>

<figure class="fifth logolar">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/dynamica-muhendislik.png" alt="Dynamica Mühendislik" class="logo-kucuk">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/kologlu-holding.png" alt="Koloğlu Holding">
</figure>
