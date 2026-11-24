---
permalink: /
title: "Shifan Liu"
heading: "About me"
excerpt: "Academic homepage of Shifan Liu"
author_profile: true
redirect_from:
  - /about/
  - /about.html
papers:
  - year: 2026
    id: cpmt
    title: "CPMT: A Collaborative Metamorphic Relations and Test Cases Prioritization Approach for Metamorphic Testing"
    authors: "Chang-ai Sun, Shifan Liu, An Fu, and Jiaming Zhang"
    venue: "Information and Software Technology"
    details: "190, Article 107975"
    doi: 10.1016/j.infsof.2025.107975
  - year: 2025
    title: "SEOCD: Detecting Obsolete Code Comments by Fusing Semantic Features and Expert Features"
    authors: "Zhanqi Cui, Shifan Liu, Li Li, and Liwei Zheng"
    venue: "Expert Systems with Applications"
    details: "280, Article 127470"
    doi: 10.1016/j.eswa.2025.127470
  - year: 2025
    title: "GITG: Automatic Issue Title Generation Method for Gitee Platform"
    authors: "Jun Yang, Shifan Liu, Xiang Chen, and Zhanqi Cui"
    venue: "Acta Electronica Sinica (电子学报)"
    details: "53(5), 1559–1570. In Chinese"
    doi: 10.12263/DZXB.20240434
  - year: 2024
    title: "MMCUP: Automatic Code Comment Updating by Fusing Multimodal Information"
    authors: "Shifan Liu, Zhanqi Cui, Xiang Chen, and Li Li"
    venue: "Chinese Journal of Computers (计算机学报)"
    details: "47(1), 172–189. In Chinese"
    doi: 10.11897/SP.J.1016.2024.00172
  - year: 2023
    title: "TBCUP: A Transformer-Based Code Comments Updating Approach"
    authors: "Shifan Liu, Zhanqi Cui, Xiang Chen, Jun Yang, Li Li, and Liwei Zheng"
    venue: "IEEE 47th Annual Computers, Software, and Applications Conference (COMPSAC)"
    details: "892–897"
    doi: 10.1109/COMPSAC57700.2023.00119
  - year: 2023
    title: "SICUP: A Comment Updating Approach based on Structural Information"
    authors: "Shifan Liu, Zhanqi Cui, and Ruilin Xie"
    venue: "International Workshop on Software Engineering & Deep Learning (SE&DL), co-located with SANER"
    details: "970–971"
    doi: 10.1109/SANER56733.2023.00118
  - year: 2023
    title: "OC-Detector: Detecting Smart Contract Vulnerabilities Based on Clustering Opcode Instructions"
    authors: "Xiguo Gu, Liwei Zheng, Huiwen Yang, Shifan Liu, and Zhanqi Cui"
    venue: "International Journal of Software Engineering and Knowledge Engineering (IJSEKE)"
    details: "33(11–12), 1673–1700"
    doi: 10.1142/S0218194023410061
  - year: 2023
    title: "Smart Contract Vulnerability Detection Based on Clustering Opcode Instructions"
    authors: "Xiguo Gu, Huiwen Yang, Shifan Liu, and Zhanqi Cui"
    venue: "International Conference on Software Engineering and Knowledge Engineering (SEKE)"
    details: "398–403"
    doi: 10.18293/SEKE2023-183
  - year: 2022
    title: "Improving Code Clone Detection Accuracy and Efficiency based on Code Complexity Analysis"
    authors: "Haochen Jin, Zhanqi Cui, Shifan Liu, and Liwei Zheng"
    venue: "International Conference on Dependable Systems and Their Applications (DSA)"
    details: "64–72"
    doi: 10.1109/DSA56465.2022.00017
---

<section id="about" class="homepage-section" markdown="1">

I am a Ph.D. student in Computer Science and Technology at the University of Science and Technology Beijing (USTB), supervised by Prof. Chang-ai Sun. I study software testing and quality assurance for deep learning frameworks and compilers. My research uses historical defects to design new tests and explores how AI can support software maintenance.

</section>

<section id="news" class="homepage-section" markdown="1">

## News {#news-heading}

<ul class="research-news">
  <li><time datetime="2026-10">Oct 2026</time><span><a href="#spectradl">SpectraDL</a> was published at ISSTA 2026.</span></li>
  <li><time datetime="2026-02">Feb 2026</time><span><a href="#cpmt">CPMT</a> was published in <em>Information and Software Technology</em>.</span></li>
</ul>

</section>

<section id="publications" class="homepage-section" markdown="1">

## Publications {#publications-heading}

<article id="spectradl" class="featured-paper" aria-labelledby="spectradl-title">
  <header class="feature-heading">
    <p class="feature-label"><strong>ISSTA 2026</strong><span aria-hidden="true"> / </span>Featured paper</p>
    <h3 id="spectradl-title">SpectraDL</h3>
    <p class="feature-subtitle">A Historical Issue-Driven, Test Specification-Assisted Transfer Testing Approach for Deep Learning Frameworks via LLMs</p>
    <p class="paper-authors"><strong>Shifan Liu</strong>, Chang-ai Sun, Fulei Wu, and Wing-Kwong Chan.</p>
  </header>
  <div class="feature-body">
    <figure class="paper-figure">
      <a href="{{ site.baseurl }}/images/spectradl-workflow.pdf" aria-label="Open the original SpectraDL workflow figure as a vector PDF">
        <img src="{{ site.baseurl }}/images/spectradl-workflow.png" width="2400" height="1611" alt="SpectraDL extracts operator test specifications, abstracts bug patterns and retrieves related operators, then generates and executes test cases." />
      </a>
      <figcaption>Figure 2. The overall workflow of SpectraDL.</figcaption>
    </figure>
    <div class="feature-notes">
      <p>SpectraDL turns historical bug reports and fixes into tests for related operators across deep learning frameworks.</p>
      <p>Across four frameworks, it found <strong>125 previously unknown bugs</strong>. Developers confirmed <strong>107</strong>.</p>
      <p class="paper-venue"><em>Proceedings of the ACM on Software Engineering</em>, vol. 3, ISSTA, 2361–2381.</p>
      <a class="read-paper" href="https://doi.org/10.1145/3832194">Read the paper <span aria-hidden="true">↗</span></a>
    </div>
  </div>
</article>

<ul class="publication-list" aria-label="Other publications">
{% assign last_year = "" %}
{% for paper in page.papers %}
  <li{% if paper.id %} id="{{ paper.id }}"{% endif %}>
    <span class="publication-year{% if last_year == paper.year %} repeated-year{% endif %}">{{ paper.year }}</span>
    {% assign last_year = paper.year %}
    <div>
      <a class="paper-title" href="https://doi.org/{{ paper.doi }}">{{ paper.title | escape }}</a>
      <p class="paper-authors">{{ paper.authors | escape | replace: "Shifan Liu", "<strong>Shifan Liu</strong>" }}.</p>
      <p class="paper-venue"><em>{{ paper.venue | escape }}</em>, {{ paper.details | escape }}.</p>
    </div>
  </li>
{% endfor %}
</ul>

</section>

<section id="education" class="homepage-section" markdown="1">

## Education {#education-heading}

<div class="education-list">
  <div class="education-item">
    <span class="education-date">2024.09-Present</span>
    <strong>Ph.D. Student, Computer Science and Technology</strong>
    <p>University of Science and Technology Beijing, Beijing, China<br>Supervisor: Prof. Chang-ai Sun.</p>
  </div>
  <div class="education-item">
    <span class="education-date">2021.09-2024.06</span>
    <strong>M.S., Computer Science and Technology</strong>
    <p>Beijing Information Science and Technology University, Beijing, China<br>Supervisor: Prof. Zhanqi Cui.</p>
  </div>
  <div class="education-item">
    <span class="education-date">2016.09-2020.06</span>
    <strong>B.Eng., Computer Science and Technology</strong>
    <p>Beijing Information Science and Technology University, Beijing, China</p>
  </div>
</div>

</section>
