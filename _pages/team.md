---
title: "MJKMH - Kişiler"
layout: gridlay
sitemap: false
permalink: /kisiler/
---

# Kişiler

{% assign number_printed = 0 %}
{% assign aktif_uyeler = site.data.team_members | where_exp: "m", "m.pasif != true" %}
{% for member in aktif_uyeler %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix team-member">
  <img src="{{ site.url }}{{ site.baseurl }}/images/kisiler/{{ member.photo | default: 'fotograf-yok.png' }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }} {{ member.surname }}, {{ member.info }}</h4>
  <ul style="overflow: hidden">
  {% for edu in member.education %}
  <li>{{ edu.level }}: {{ edu.university }}{% if site.team_show_department and edu.department %}, {{ edu.department }}{% endif %}{% if site.team_show_years and edu.years %}, {{ edu.years }}{% endif %}</li>
  {% endfor %}
  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<hr>

{% assign bolumler = "misafir:Misafir Araştırmacılar,lisansustu:Doktora ve Yüksek Lisans Öğrencileri,lisans:Lisans Öğrencileri" | split: "," %}
{% for bolum in bolumler %}
{% assign parca = bolum | split: ":" %}
<h2 class="kisi-bolum">{{ parca[1] }}</h2>
<div class="row">
{% assign anahtar = parca[0] %}
{% for kisi in site.data.ogrenciler[anahtar] %}
<div class="col-sm-6 clearfix team-member{% if anahtar != 'misafir' %} ogrenci{% endif %}">
  <img src="{{ site.url }}{{ site.baseurl }}/images/kisiler/{{ kisi.photo | default: 'fotograf-yok.png' }}" class="img-responsive" width="{% if anahtar == 'misafir' %}25%{% else %}18%{% endif %}" style="float: left" />
  <h4>{{ kisi.name }} {{ kisi.surname }}{% if kisi.info %}, {{ kisi.info }}{% endif %}</h4>
  {% if kisi.institution %}<ul style="overflow: hidden"><li>{{ kisi.institution }}</li></ul>{% endif %}
  {% if kisi.advisor %}<p class="danisman">Danışman: {{ kisi.advisor }}</p>{% endif %}
</div>
{% endfor %}
</div>
<hr>
{% endfor %}

<h2 class="kisi-bolum" id="mezunlar">Mezunlar</h2>

{% assign lisans = site.data.mezunlar.lisans %}
{% assign yarim = lisans.size | plus: 1 | divided_by: 2 %}
<div class="row mezunlar">
<div class="col-sm-3">
<h3 class="kisi-bolum">Doktora</h3>
<ul>{% for kisi in site.data.mezunlar.doktora %}<li>{{ kisi.name }} {{ kisi.surname }}{% if kisi.year %}, {{ kisi.year }}{% endif %}{% if kisi.advisor %}<br><span class="danisman">Danışman: {{ kisi.advisor }}</span>{% endif %}</li>{% endfor %}</ul>
</div>
<div class="col-sm-3">
<h3 class="kisi-bolum">Yüksek Lisans</h3>
<ul>{% for kisi in site.data.mezunlar.yuksek_lisans %}<li>{{ kisi.name }} {{ kisi.surname }}{% if kisi.year %}, {{ kisi.year }}{% endif %}{% if kisi.advisor %}<br><span class="danisman">Danışman: {{ kisi.advisor }}</span>{% endif %}</li>{% endfor %}</ul>
</div>
<div class="col-sm-3">
<h3 class="kisi-bolum">Lisans</h3>
<ul>{% for kisi in lisans limit: yarim %}<li>{{ kisi.name }} {{ kisi.surname }}{% if kisi.year %}, {{ kisi.year }}{% endif %}{% if kisi.advisor %}<br><span class="danisman">Danışman: {{ kisi.advisor }}</span>{% endif %}</li>{% endfor %}</ul>
</div>
<div class="col-sm-3">
<h3 class="kisi-bolum mezun-bos-baslik">&nbsp;</h3>
<ul>{% for kisi in lisans offset: yarim %}<li>{{ kisi.name }} {{ kisi.surname }}{% if kisi.year %}, {{ kisi.year }}{% endif %}{% if kisi.advisor %}<br><span class="danisman">Danışman: {{ kisi.advisor }}</span>{% endif %}</li>{% endfor %}</ul>
</div>
</div>
