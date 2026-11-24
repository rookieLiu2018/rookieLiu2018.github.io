---
permalink: /
title: "Shifan Liu"
heading: "About"
author_profile: true
excerpt: "Academic homepage of Shifan Liu"
redirect_from:
  - /about/
  - /about.html
papers:
  - year: 2026
    id: spectradl
    title: "SpectraDL: A Historical Issue-Driven, Test Specification-Assisted Transfer Testing Approach for Deep Learning Frameworks via LLMs"
    authors: "Shifan Liu, Chang-ai Sun, Fulei Wu, and Wing-Kwong Chan"
    venue: "Proceedings of the ACM on Software Engineering"
    details: "vol. 3, ISSTA 2026, 2361–2381"
    doi: 10.1145/3832194
    figure: /images/spectradl-workflow.pdf
    thumbnail: /images/spectradl-workflow.png
  - year: 2026
    id: cpmt
    title: "CPMT: A Collaborative Metamorphic Relations and Test Cases Prioritization Approach for Metamorphic Testing"
    authors: "Chang-ai Sun, Shifan Liu, An Fu, and Jiaming Zhang"
    venue: "Information and Software Technology"
    details: "190, Article 107975"
    doi: 10.1016/j.infsof.2025.107975
  - year: 2025
    id: seocd
    title: "SEOCD: Detecting Obsolete Code Comments by Fusing Semantic Features and Expert Features"
    authors: "Zhanqi Cui, Shifan Liu, Li Li, and Liwei Zheng"
    venue: "Expert Systems with Applications"
    details: "280, Article 127470"
    doi: 10.1016/j.eswa.2025.127470
  - year: 2025
    original_title: "GITG：面向Gitee平台的issue标题自动生成方法"
    title: "GITG: Automatic Issue Title Generation Method for Gitee Platform"
    authors: "Jun Yang, Shifan Liu, Xiang Chen, and Zhanqi Cui"
    venue: "Acta Electronica Sinica (电子学报)"
    details: "53(5), 1559–1570. In Chinese"
    doi: 10.12263/DZXB.20240434
  - year: 2024
    id: mmcup
    original_title: "MMCUP：融合多模态信息的代码注释自动更新方法"
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

I am a Ph.D. student in Computer Science and Technology at the University of Science and Technology Beijing (USTB), supervised by Prof. Chang-ai Sun.

My research focuses on the reliability of deep learning systems. I develop automated testing techniques for frameworks and compilers, and I study how bugs in these systems affect the applications built on them.

</section>

<section id="news" class="homepage-section" markdown="1">

## News {#news-heading}

<ul class="news-list">
  <li><time class="news-date" datetime="2026-11">Nov 2026</time><span>I’m visiting <a href="https://haoyetiancoder.github.io/">Professor Tian Haoye</a>’s group at Aalto University through December.</span></li>
  <li><time class="news-date" datetime="2026-10">Oct 2026</time><span>Our paper <a href="#spectradl">SpectraDL</a> appeared at ISSTA 2026.</span></li>
  <li><time class="news-date" datetime="2026-02">Feb 2026</time><span>Our paper <a href="#cpmt">CPMT</a> appeared in <em>Information and Software Technology</em>.</span></li>
</ul>

</section>

<section id="publications" class="homepage-section" markdown="1">

## Publications {#publications-heading}

<ul class="publication-list" aria-label="Publications by year">
{% assign previous_year = nil %}
{% for paper in page.papers %}
  <li class="publication{% unless paper.year == previous_year %} year-start{% endunless %}"{% if paper.id %} id="{{ paper.id }}"{% endif %}>
    <span class="pub-year{% if paper.year == previous_year %} repeat-year{% endif %}">{{ paper.year }}</span>
    {% assign previous_year = paper.year %}
    <div class="pub-info">
      <h3><a href="https://doi.org/{{ paper.doi }}"{% if paper.original_title %} lang="zh" title="{{ paper.title | escape }}"{% endif %}>{{ paper.original_title | default: paper.title | escape }}</a></h3>
      <p class="authors">{{ paper.authors | escape | replace: "Shifan Liu", "<strong>Shifan Liu</strong>" }}.</p>
      <p class="citation"><em>{{ paper.venue | escape }}</em>, {{ paper.details | escape }}.</p>
      {% if paper.figure %}
      <div class="paper-description">
        <div>
          <p>SpectraDL uses an LLM to extract bug patterns from past reports and fixes. It matches patterns to operators with similar behavior and input constraints, then generates tests for those operators.</p>
          <p>Starting with 419 reports from PyTorch and TensorFlow, we tested those two frameworks as well as PaddlePaddle and MindSpore. SpectraDL found <strong>125 previously unknown bugs</strong>, of which developers confirmed <strong>107</strong>.</p>
        </div>
        <figure class="workflow">
          <a href="{{ site.baseurl }}{{ paper.figure }}" aria-label="Open Figure 2 from SpectraDL (PDF)">
            <img src="{{ site.baseurl }}{{ paper.thumbnail }}" width="2400" height="1611" alt="SpectraDL workflow from bug reports and operator specifications to generated tests." />
            <span>Figure 2 <i class="fas fa-expand" aria-hidden="true"></i></span>
          </a>
        </figure>
      </div>
      {% endif %}
    </div>
  </li>
{% endfor %}
</ul>

</section>

<section id="contributions" class="homepage-section" markdown="1">

## Open-source contributions {#contributions-heading}

We have reported **218 bugs** to [PyTorch](https://github.com/pytorch/pytorch/issues/141487), [TensorFlow](https://github.com/tensorflow/tensorflow/issues/94657), [PaddlePaddle](https://github.com/PaddlePaddle/Paddle/issues/75189), [MindSpore](https://gitee.com/mindspore/mindspore/issues/ICU4KB), and [ONNX Runtime](https://github.com/microsoft/onnxruntime/issues/33244). Project maintainers have confirmed **187** of them.

</section>
