---
title: "MJKMH - Laboratuvarlar"
layout: textlay
sitemap: false
permalink: /laboratuvarlar/
---

# Laboratuvarlar

{% for l in site.data.laboratuvarlar %}
<div markdown="0" class="row laboratuvar">
{% if l.image %}<div class="col-sm-4"><img src="{{ site.url }}{{ site.baseurl }}/images/laboratuvarlar/{{ l.image }}" class="img-responsive" alt="{{ l.name }}" /></div><div class="col-sm-8">{% else %}<div class="col-sm-12">{% endif %}
<h2 class="kisi-bolum">{{ l.name }}</h2>
{% if l.text %}{{ l.text | markdownify }}{% endif %}
</div>
</div>
{% endfor %}
