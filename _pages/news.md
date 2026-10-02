---
layout: archive
title: "News"
permalink: /news/
author_profile: true
---

{% comment %}Edit _data/news.yml to add news (newest first).{% endcomment %}
<ul class="news-list">
{% for item in site.data.news %}
  <li><strong>{{ item.title | markdownify | remove: "<p>" | remove: "</p>" | strip }}</strong>: {{ item.text | markdownify | remove: "<p>" | remove: "</p>" }}</li>
{% endfor %}
</ul>
