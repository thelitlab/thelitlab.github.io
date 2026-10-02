---
permalink: /
title: "LIT @UNT"
excerpt: "LIT Lab at the University of North Texas"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

The **LIT (Language, Interpretability, and Trust)** group is part of the [Department of Computer Science and Engineering at the University of North Texas](https://computerscience.engineering.unt.edu/). We study how language models use information, how their outputs should be evaluated, and how supervision can improve their behavior.

Our research connects three areas:

- **Understanding model behavior:** investigating representations, reasoning, and whether explanations faithfully reflect the information and computations behind a model's decisions.
- **Evaluation and learning from feedback:** developing datasets and methods for human-preference evaluation, rubric-based assessment, and LLM judges, and studying how models learn from this supervision.
- **Language technologies for scientific knowledge:** extracting and assessing information in scientific documents, including figures and tables, hallucinations, reproducibility, and research limitations.

Our work spans long-form question answering, student response assessment, and scientific information processing.
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
