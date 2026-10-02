---
permalink: /
title: ""
excerpt: "LIT Group at the University of North Texas"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

The **LIT (Language, Interpretability, and Trust)** group is part of the [Department of Computer Science and Engineering at the University of North Texas](https://computerscience.engineering.unt.edu/). We study how language models use information, how their outputs should be evaluated, and how supervision can improve their behavior.

<figure class="research-overview research-overview--wide">
  <a href="{{ base_path }}/research/"><img src="{{ base_path }}/images/research/overview.svg" alt="Interpretability at the center, connecting four problem areas: evaluation and peer review; generalization in NLP tasks; computational social science and the reliability of survey instruments; and law, governance and compliance."></a>
</figure>

See our [people]({{ base_path }}/people/), [research]({{ base_path }}/research/) and [publications]({{ base_path }}/publications/).

### Funding

Our work is supported by:

<div class="funders">
{% for f in site.data.funding %}
  <div class="funder">
    <a href="{{ f.url }}" class="funder__logo"><img src="{{ base_path }}/images/funding/{{ f.logo }}" alt="{{ f.name }}"></a>
    <!--ul class="funder__grants">
    {% for g in f.grants %}<li>{{ g | markdownify | remove: "<p>" | remove: "</p>" | strip }}</li>{% endfor %}
    </ul-->
  </div>
{% endfor %}
</div>

### News

<ul class="news-list">
{% for item in site.data.news limit: 6 %}
  <li><strong>{{ item.title | markdownify | remove: "<p>" | remove: "</p>" | strip }}</strong>: {{ item.text | markdownify | remove: "<p>" | remove: "</p>" }}</li>
{% endfor %}
</ul>
[All news →]({{ base_path }}/news/)

### From the blog

{% for post in site.posts limit: 3 %}
  {% include archive-single.html %}
{% else %}
No posts yet.
{% endfor %}
[All posts →]({{ base_path }}/blog/)
