---
permalink: /
title: "LIT Lab"
excerpt: "LIT Lab at the University of North Texas"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

The LIT Lab (Language, Interpretability and Trust) is part of the [Department of Computer Science and Engineering, University of North Texas](https://computerscience.engineering.unt.edu/), led by [Sagnik Ray Choudhury](https://sagnikrayc.xyz/). We work on two broad themes:

1. **Explaining the behavior and limitations of LLMs**, with a focus on [model bias](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0277640) and [reasoning abilities](https://aclanthology.org/2022.coling-1.8/).
2. **Scholarly information processing** to enhance users' experience with digital libraries: e.g. [extracting information from scientific figures](https://dl.acm.org/doi/pdf/10.1145/2928294.2928305), [understanding reproducibility of scientific articles](https://dl.acm.org/doi/pdf/10.1145/3627673.3679831), and [automatically generating limitations of scientific papers](https://arxiv.org/pdf/2505.18207).

See our [people]({{ base_path }}/people/), [research]({{ base_path }}/research/) and [publications]({{ base_path }}/publications/).

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
