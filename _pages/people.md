---
layout: archive
title: "People"
permalink: /people/
author_profile: false
---

{% comment %}Edit _data/authors.yml to add or update lab members.{% endcomment %}
{% include base_path %}

{% assign groups = "pi:Principal Investigator|postdoc:Postdocs|phd:PhD Students|ms:Master's Students|undergrad:Undergraduates|alumni:Alumni" | split: "|" %}
{% for g in groups %}
  {% assign gid = g | split: ":" | first %}
  {% assign glabel = g | split: ":" | last %}
  {% assign members = "" | split: "" %}
  {% for pair in site.data.authors %}
    {% if pair[1].group == gid %}{% assign members = members | push: pair %}{% endif %}
  {% endfor %}
  {% if members.size > 0 %}
<h2 class="archive__subtitle">{{ glabel }}</h2>
<div class="people-grid">
  {% for pair in members %}
    {% assign m = pair[1] %}
    {% if m.avatar contains "://" %}{% assign av = m.avatar %}{% else %}{% assign av = m.avatar | default: "people/placeholder.jpg" | prepend: "/images/" | prepend: base_path %}{% endif %}
  <div class="person" id="{{ pair[0] }}">
    <img src="{{ av }}" alt="{{ m.name }}">
    <h3 class="person__name">{% if m.uri %}<a href="{{ m.uri }}">{{ m.name }}</a>{% else %}{{ m.name }}{% endif %}</h3>
    {% if m.position %}<p class="person__position">{{ m.position }}</p>{% endif %}
    {% if m.now %}<p class="person__now">Now: {{ m.now }}</p>{% endif %}
    <p class="person__links">
      {% if m.email %}<a href="mailto:{{ m.email }}" title="Email"><i class="fas fa-envelope"></i></a>{% endif %}
      {% if m.github %}<a href="https://github.com/{{ m.github }}" title="GitHub"><i class="fab fa-github"></i></a>{% endif %}
      {% if m.googlescholar %}<a href="{{ m.googlescholar }}" title="Google Scholar"><i class="fas fa-graduation-cap"></i></a>{% endif %}
      {% if m.linkedin %}<a href="https://www.linkedin.com/in/{{ m.linkedin }}" title="LinkedIn"><i class="fab fa-linkedin"></i></a>{% endif %}
    </p>
  </div>
  {% endfor %}
</div>
  {% endif %}
{% endfor %}
