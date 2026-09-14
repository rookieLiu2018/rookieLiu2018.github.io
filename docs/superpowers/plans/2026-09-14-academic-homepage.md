# Academic Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the outdated generated homepage with a white-only, Academic Pages-based personal academic site for Shifan Liu, styled after the compact sidebar-and-content hierarchy of `samxrl.github.io`.

**Architecture:** Preserve `rookieLiu2018/rookieLiu2018.github.io` and its history as the deployment repository while creating `rookieLiu2018/academicpages.github.io` as the requested upstream fork. Import the forked Jekyll template into the existing feature branch, then reduce it to one homepage with anchored About, Publications, and Education sections. Keep identity data in `_config.yml`, content in `_pages/about.md`, presentation overrides in `_sass/_custom.scss`, and the supplied portrait as `images/profile.jpg`.

**Tech Stack:** GitHub Pages, Jekyll, Academic Pages, Markdown/Kramdown, SCSS, GitHub Actions, Python standard-library contract tests, Docker for the local Jekyll build when available.

---

## File Map

- `AGENTS.md` and the Academic Pages theme files: imported unchanged from the fork unless a later task names them explicitly.
- `_config.yml`: site identity, URL, repository, author sidebar, light-theme selection, and disabled unused features.
- `_data/navigation.yml`: same-page navigation anchors only.
- `_pages/about.md`: all public biography, research-interest, publication, and education content.
- `_includes/masthead.html`: remove the theme-switch control.
- `assets/css/main.scss`: load only the light theme and the site-specific overrides.
- `_sass/theme/_default_light.scss`: white, navy, charcoal, and gray color tokens.
- `_sass/_custom.scss`: compact reference-inspired layout, portrait crop, publication hierarchy, responsive behavior, and focus styles.
- `images/profile.jpg`: the exact user-supplied photograph; no generative or destructive edit.
- `images/favicon.svg`: simple `SL` monogram favicon on white/navy.
- `tests/test_site_contract.py`: regression checks for required content, exclusions, navigation, portrait, and white-only theming.
- `docs/superpowers/specs/2026-09-14-academic-homepage-design.md`: approved design record, preserved during the template import.
- `docs/superpowers/plans/2026-09-14-academic-homepage.md`: this execution plan, preserved during the template import.

### Task 1: Create the Fork and Import Academic Pages

**Files:**
- Replace tracked legacy site paths: `2024/`, `404.html`, `archives/`, `attaches/`, `css/`, `images/`, `img/`, `index.html`, `js/`, `lib/`
- Import: Academic Pages repository tree
- Preserve: `docs/superpowers/**`

- [ ] **Step 1: Verify the feature branch and clean worktree**

Run:

```powershell
git branch --show-current
git status --short
```

Expected: branch is `codex/academic-homepage`; output contains no uncommitted changes.

- [ ] **Step 2: Create or reuse the requested GitHub fork**

Run:

```powershell
gh repo view rookieLiu2018/academicpages.github.io --json isFork,parent 2>$null
```

If it does not exist, run:

```powershell
gh repo fork academicpages/academicpages.github.io --clone=false --remote=false
```

Expected: `rookieLiu2018/academicpages.github.io` exists and reports `academicpages/academicpages.github.io` as its parent.

- [ ] **Step 3: Fetch the fork as the template source**

Run:

```powershell
git remote add academicpages-fork https://github.com/rookieLiu2018/academicpages.github.io.git
git fetch academicpages-fork master
```

If the remote already exists, verify it with `git remote get-url academicpages-fork` and run only the fetch. Expected: `academicpages-fork/master` resolves successfully.

- [ ] **Step 4: Remove only the legacy generated-site tree**

Run:

```powershell
git rm -r -- 2024 404.html archives attaches css images img index.html js lib
```

Expected: only the listed legacy site paths are staged for deletion; `docs/superpowers/**` remains present.

- [ ] **Step 5: Import the forked template tree**

Run:

```powershell
git checkout academicpages-fork/master -- .
git status --short
```

Expected: Academic Pages files such as `_config.yml`, `_pages/about.md`, `Gemfile`, and `.github/workflows/jekyll-build.yml` are staged; both design and plan documents remain present.

- [ ] **Step 6: Commit the template foundation**

Run:

```powershell
git add --all
git commit -m "chore: adopt Academic Pages foundation"
```

Expected: one commit containing the fork-derived foundation and removal of the old generated site.

### Task 2: Add a Failing Site Contract Test

**Files:**
- Create: `tests/test_site_contract.py`

- [ ] **Step 1: Create the contract test**

Add this complete file:

```python
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class AcademicHomepageContract(unittest.TestCase):
    def read(self, relative_path: str) -> str:
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_identity_and_navigation(self):
        config = self.read("_config.yml")
        navigation = self.read("_data/navigation.yml")
        self.assertIn('title                    : "Shifan Liu"', config)
        self.assertIn('repository               : "rookieLiu2018/rookieLiu2018.github.io"', config)
        self.assertIn('avatar           : "profile.jpg"', config)
        self.assertIn('github           : "rookieLiu2018"', config)
        self.assertIn('url: /#about', navigation)
        self.assertIn('url: /#publications', navigation)
        self.assertIn('url: /#education', navigation)
        self.assertNotIn('/cv/', navigation.lower())

    def test_homepage_contains_only_approved_sections(self):
        page = self.read("_pages/about.md")
        for section_id in ('id="about"', 'id="publications"', 'id="education"'):
            self.assertIn(section_id, page)
        for doi in (
            "10.1145/3832194",
            "10.1016/j.infsof.2025.107975",
            "10.1016/j.eswa.2025.127470",
            "10.11897/SP.J.1016.2024.00172",
            "10.1109/COMPSAC57700.2023.00119",
        ):
            self.assertIn(doi, page)
        forbidden = ("Research Experience", "Awards", "Honors", "Download CV")
        for phrase in forbidden:
            self.assertNotIn(phrase, page)

    def test_portrait_and_light_theme(self):
        self.assertTrue((ROOT / "images/profile.jpg").is_file())
        self.assertGreater((ROOT / "images/profile.jpg").stat().st_size, 100_000)
        main_scss = self.read("assets/css/main.scss")
        masthead = self.read("_includes/masthead.html")
        custom = self.read("_sass/_custom.scss")
        self.assertNotIn("append: '_dark'", main_scss)
        self.assertNotIn('id="theme-toggle"', masthead)
        self.assertIn("--global-bg-color", self.read("_sass/theme/_default_light.scss"))
        self.assertIn("background: #fff", custom)

    def test_example_content_is_removed(self):
        for dirname in ("_posts", "_talks", "_teaching", "_portfolio", "_publications"):
            directory = ROOT / dirname
            self.assertFalse(directory.exists() and any(directory.iterdir()), dirname)
        self.assertFalse((ROOT / "_pages/cv.md").exists())
        self.assertFalse((ROOT / "_pages/publications.html").exists())


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test and verify the imported template fails the contract**

Run:

```powershell
python -m unittest tests.test_site_contract -v
```

Expected: failures for template placeholder identity, missing homepage sections, absent user portrait, dark-theme import/toggle, and sample content.

- [ ] **Step 3: Commit the failing contract**

Run:

```powershell
git add tests/test_site_contract.py
git commit -m "test: define academic homepage content contract"
```

### Task 3: Configure Identity, Navigation, and Portrait

**Files:**
- Modify: `_config.yml`
- Modify: `_data/navigation.yml`
- Create: `images/profile.jpg`

- [ ] **Step 1: Replace the site and author identity in `_config.yml`**

Set the basic site values to:

```yaml
locale                   : "en-US"
site_theme               : "default"
title                    : "Shifan Liu"
title_separator          : "-"
name                     : &name "Shifan Liu"
description              : &description "Academic homepage of Shifan Liu, a Ph.D. student researching software testing and quality assurance for deep learning systems."
url                      : "https://rookieLiu2018.github.io"
baseurl                  : ""
repository               : "rookieLiu2018/rookieLiu2018.github.io"
```

Replace the complete `author:` mapping with:

```yaml
author:
  avatar           : "profile.jpg"
  name             : "Shifan Liu"
  pronouns         :
  bio              : "Ph.D. Student in Computer Science and Technology"
  location         : "Beijing, China"
  employer         : "University of Science and Technology Beijing"
  uri              :
  email            : "sfliu@xs.ustb.edu.cn"
  academia         :
  arxiv            :
  googlescholar    :
  inspire-hep      :
  impactstory      :
  orcid            :
  semantic         :
  ssrn             :
  pubmed           :
  researchgate     :
  scopus           :
  zotero           :
  bitbucket        :
  codepen          :
  dribbble         :
  github           : "rookieLiu2018"
  kaggle           :
  stackoverflow    :
  artstation       :
  bluesky          :
  facebook         :
  flickr           :
  foursquare       :
  goodreads        :
  google_plus      :
  keybase          :
  instagram        :
  lastfm           :
  linkedin         :
  mastodon         :
  medium           :
  pinterest        :
  soundcloud       :
  steam            :
  telegram         :
  tumblr           :
  twitter          :
  vine             :
  weibo            :
  wikipedia        :
  xing             :
  youtube          :
  zhihu            :
```

Also set `atom_feed.hide: true`, keep analytics disabled, and leave `og_image` empty because no social-preview image was requested.

- [ ] **Step 2: Replace navigation with homepage anchors**

Replace `_data/navigation.yml` with:

```yaml
main:
  - title: "Home"
    url: /
  - title: "About"
    url: /#about
  - title: "Publications"
    url: /#publications
  - title: "Education"
    url: /#education
```

- [ ] **Step 3: Copy the approved portrait without altering it**

Run:

```powershell
Copy-Item -LiteralPath 'C:\Users\liu\AppData\Local\Temp\codex-clipboard-bacc5d6d-c22a-4a5e-9696-a39e0fb5875f.jpg' -Destination 'C:\Users\liu\Documents\ChatGPT\website\images\profile.jpg'
```

Expected: `images/profile.jpg` exists, is 340211 bytes, and remains a JPEG. Cropping will be visual-only through CSS.

- [ ] **Step 4: Run the focused identity test**

Run:

```powershell
python -m unittest tests.test_site_contract.AcademicHomepageContract.test_identity_and_navigation -v
```

Expected: PASS.

- [ ] **Step 5: Commit identity and navigation**

Run:

```powershell
git add _config.yml _data/navigation.yml images/profile.jpg
git commit -m "feat: configure academic identity and navigation"
```

### Task 4: Write the Approved Homepage Content

**Files:**
- Modify: `_pages/about.md`

- [ ] **Step 1: Replace `_pages/about.md` with the complete homepage**

Use this content:

```markdown
---
permalink: /
title: "Shifan Liu"
excerpt: "Academic homepage of Shifan Liu"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<section id="about" class="homepage-section" markdown="1">

I am a Ph.D. student in Computer Science and Technology at the University of Science and Technology Beijing (USTB), supervised by Prof. Chang-ai Sun. My research focuses on software testing and quality assurance for deep learning frameworks and compilers, with particular interests in historical-defect-driven testing and AI-assisted software maintenance.

### Research Interests

- Software Testing
- Deep Learning Framework and Compiler Quality Assurance
- Historical-Defect-Driven Testing

</section>

<section id="publications" class="homepage-section" markdown="1">

## Publications

<ol class="publication-list">
  <li>
    <span class="publication-year">2026</span>
    <div><a href="https://doi.org/10.1145/3832194"><strong>SpectraDL: A Historical Issue-Driven, Test Specification-Assisted Transfer Testing Approach for Deep Learning Frameworks via LLMs</strong></a><br><strong>Shifan Liu</strong>, Chang-ai Sun, Fulei Wu, and Wing-Kwong Chan.<br><em>Proceedings of the ACM on Software Engineering</em>, vol. 3, ISSTA, Article ISSTA103. Accepted research paper at ISSTA 2026.</div>
  </li>
  <li>
    <span class="publication-year">2026</span>
    <div><a href="https://doi.org/10.1016/j.infsof.2025.107975"><strong>CPMT: A Collaborative Metamorphic Relations and Test Cases Prioritization Approach for Metamorphic Testing</strong></a><br>Chang-ai Sun, <strong>Shifan Liu</strong>, An Fu, and Jiaming Zhang.<br><em>Information and Software Technology</em>, vol. 190, Article 107975.</div>
  </li>
  <li>
    <span class="publication-year">2025</span>
    <div><a href="https://doi.org/10.1016/j.eswa.2025.127470"><strong>SEOCD: Detecting Obsolete Code Comments by Fusing Semantic Features and Expert Features</strong></a><br>Zhanqi Cui, <strong>Shifan Liu</strong>, Li Li, and Liwei Zheng.<br><em>Expert Systems with Applications</em>, vol. 280, Article 127470.</div>
  </li>
  <li>
    <span class="publication-year">2024</span>
    <div><a href="https://doi.org/10.11897/SP.J.1016.2024.00172"><strong>MMCUP: Automatic Code Comment Updating by Fusing Multimodal Information</strong></a><br><strong>Shifan Liu</strong>, Zhanqi Cui, Xiang Chen, and Li Li.<br><em>Chinese Journal of Computers</em>, vol. 47, no. 1, pp. 172-189. In Chinese.</div>
  </li>
  <li>
    <span class="publication-year">2023</span>
    <div><a href="https://doi.org/10.1109/COMPSAC57700.2023.00119"><strong>TBCUP: A Transformer-Based Code Comments Updating Approach</strong></a><br><strong>Shifan Liu</strong>, Zhanqi Cui, Xiang Chen, Jun Yang, Li Li, and Liwei Zheng.<br><em>2023 IEEE 47th Annual Computers, Software, and Applications Conference (COMPSAC)</em>, pp. 892-897.</div>
  </li>
</ol>

</section>

<section id="education" class="homepage-section" markdown="1">

## Education

<div class="education-list">
  <div class="education-item"><span>2024.09-Present</span><strong>Ph.D. Student, Computer Science and Technology</strong><p>University of Science and Technology Beijing, Beijing, China<br>Supervisor: Prof. Chang-ai Sun</p></div>
  <div class="education-item"><span>2021.09-2024.06</span><strong>M.S., Computer Science and Technology</strong><p>Beijing Information Science and Technology University, Beijing, China<br>Supervisor: Prof. Zhanqi Cui</p></div>
  <div class="education-item"><span>2016.09-2020.06</span><strong>B.Eng., Computer Science and Technology</strong><p>Beijing Information Science and Technology University, Beijing, China</p></div>
</div>

</section>
```

- [ ] **Step 2: Run the homepage-content test**

Run:

```powershell
python -m unittest tests.test_site_contract.AcademicHomepageContract.test_homepage_contains_only_approved_sections -v
```

Expected: PASS.

- [ ] **Step 3: Commit the homepage content**

Run:

```powershell
git add _pages/about.md
git commit -m "feat: add verified academic profile content"
```

### Task 5: Enforce the White-Only Reference-Inspired Presentation

**Files:**
- Modify: `_includes/masthead.html`
- Modify: `assets/css/main.scss`
- Modify: `_sass/theme/_default_light.scss`
- Create: `_sass/_custom.scss`

- [ ] **Step 1: Remove the theme toggle from `_includes/masthead.html`**

Delete only this list item:

```html
<li id="theme-toggle" class="masthead__menu-item persist tail">
  <a role="button" aria-labelledby="theme-icon"><i id="theme-icon" class="fa-solid fa-sun" aria-hidden="true" title="toggle theme"></i></a>
</li>
```

- [ ] **Step 2: Stop compiling the dark theme and load custom overrides**

In `assets/css/main.scss`, remove:

```scss
"theme/{{ site.site_theme | default: 'default' | append: '_dark' }}",
```

Append `"custom"` as the last import entry so the closing portion becomes:

```scss
    "layout/archive",
    "layout/sidebar",
    "layout/json_cv",
    "custom"
;
```

- [ ] **Step 3: Set the light palette in `_sass/theme/_default_light.scss`**

Use these principal values while retaining the existing variable names:

```scss
$primary-color              : #173f6b;
$gray                       : #68717d;

:root {
    --global-base-color                 : #173f6b;
    --global-bg-color                   : #fff;
    --global-footer-bg-color            : #fff;
    --global-border-color               : #e7e9ed;
    --global-dark-border-color          : #d4d8de;
    --global-code-background-color      : #f7f8fa;
    --global-code-text-color            : #24292f;
    --global-fig-caption-color          : #68717d;
    --global-link-color                 : #245f9e;
    --global-link-color-hover           : #173f6b;
    --global-link-color-visited         : #245f9e;
    --global-masthead-link-color        : #3e4650;
    --global-masthead-link-color-hover  : #173f6b;
    --global-text-color                 : #24292f;
    --global-text-color-light           : #68717d;
    --global-thead-color                : #f7f8fa;
}
```

- [ ] **Step 4: Create `_sass/_custom.scss`**

Add:

```scss
html {
  scroll-behavior: smooth;
  background: #fff;
}

body {
  background: #fff;
  font-size: 16px;
  line-height: 1.7;
}

.masthead {
  background: rgba(255, 255, 255, 0.97);
  border-bottom: 1px solid var(--global-border-color);
  box-shadow: none;
}

.masthead__menu-item a {
  font-weight: 500;
}

.page__title {
  margin-bottom: 1.25rem;
  color: #173f6b;
  font-size: clamp(1.75rem, 4vw, 2.35rem);
}

.author__avatar img {
  aspect-ratio: 1 / 1;
  width: 190px;
  height: 190px;
  object-fit: cover;
  object-position: 50% 42%;
  border: 1px solid #e1e4e8;
  border-radius: 50%;
  box-shadow: none;
}

.author__name {
  color: #173f6b;
  font-size: 1.35rem;
}

.homepage-section {
  scroll-margin-top: 6rem;
  margin-bottom: 3rem;
}

.homepage-section h2 {
  margin-top: 2.75rem;
  padding-bottom: 0.45rem;
  border-bottom: 1px solid var(--global-border-color);
  color: #173f6b;
  font-size: 1.55rem;
}

.homepage-section h3 {
  color: #173f6b;
  font-size: 1.15rem;
}

.publication-list {
  margin-left: 0;
  padding-left: 0;
  list-style: none;
}

.publication-list li {
  display: grid;
  grid-template-columns: 4.25rem minmax(0, 1fr);
  gap: 1rem;
  padding: 1.15rem 0;
  border-bottom: 1px solid var(--global-border-color);
}

.publication-year {
  color: #68717d;
  font-variant-numeric: tabular-nums;
  font-weight: 600;
}

.education-item {
  display: grid;
  grid-template-columns: 10rem minmax(0, 1fr);
  gap: 0.2rem 1.25rem;
  padding: 1rem 0;
  border-bottom: 1px solid var(--global-border-color);
}

.education-item > span {
  grid-row: 1 / span 2;
  color: #68717d;
  font-variant-numeric: tabular-nums;
}

.education-item p {
  margin: 0.2rem 0 0;
}

a:focus-visible,
button:focus-visible {
  outline: 3px solid rgba(36, 95, 158, 0.35);
  outline-offset: 3px;
}

@media (max-width: 767px) {
  .author__avatar img {
    width: 136px;
    height: 136px;
  }

  .publication-list li,
  .education-item {
    grid-template-columns: 1fr;
    gap: 0.35rem;
  }

  .education-item > span {
    grid-row: auto;
  }
}
```

- [ ] **Step 5: Run the portrait and light-theme test**

Run:

```powershell
python -m unittest tests.test_site_contract.AcademicHomepageContract.test_portrait_and_light_theme -v
```

Expected: PASS.

- [ ] **Step 6: Commit the presentation changes**

Run:

```powershell
git add _includes/masthead.html assets/css/main.scss _sass/theme/_default_light.scss _sass/_custom.scss
git commit -m "style: create white academic homepage presentation"
```

### Task 6: Remove Template Examples and Add a Site Favicon

**Files:**
- Delete: `_drafts/`, `_posts/`, `_portfolio/`, `_publications/`, `_talks/`, `_teaching/`, `files/`, `markdown_generator/`, `talkmap/`, `talkmap.py`, `talkmap.ipynb`, `talkmap_out.ipynb`
- Delete: `_pages/archive-layout-with-content.md`, `_pages/category-archive.html`, `_pages/collection-archive.html`, `_pages/cv-json.md`, `_pages/cv.md`, `_pages/markdown.md`, `_pages/non-menu-page.md`, `_pages/page-archive.html`, `_pages/portfolio.html`, `_pages/publications.html`, `_pages/tag-archive.html`, `_pages/talkmap.html`, `_pages/talks.html`, `_pages/teaching.html`, `_pages/terms.md`, `_pages/year-archive.html`
- Modify: `images/favicon.svg`

- [ ] **Step 1: Remove the explicitly unused example content**

Run:

```powershell
git rm -r -- _drafts _posts _portfolio _publications _talks _teaching files markdown_generator talkmap talkmap.py talkmap.ipynb talkmap_out.ipynb _pages/archive-layout-with-content.md _pages/category-archive.html _pages/collection-archive.html _pages/cv-json.md _pages/cv.md _pages/markdown.md _pages/non-menu-page.md _pages/page-archive.html _pages/portfolio.html _pages/publications.html _pages/tag-archive.html _pages/talkmap.html _pages/talks.html _pages/teaching.html _pages/terms.md _pages/year-archive.html
```

Expected: no example post, publication, talk, teaching, portfolio, CV, guide, or sample PDF remains available as a generated page.

- [ ] **Step 2: Replace `images/favicon.svg` with the site monogram**

Use:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#ffffff"/>
  <rect x="2" y="2" width="60" height="60" rx="10" fill="none" stroke="#173f6b" stroke-width="4"/>
  <text x="32" y="41" text-anchor="middle" font-family="Arial, sans-serif" font-size="27" font-weight="700" fill="#173f6b">SL</text>
</svg>
```

- [ ] **Step 3: Run the example-content test and full contract**

Run:

```powershell
python -m unittest tests.test_site_contract.AcademicHomepageContract.test_example_content_is_removed -v
python -m unittest discover -s tests -v
```

Expected: the focused test passes, then all four contract tests pass.

- [ ] **Step 4: Commit cleanup and favicon**

Run:

```powershell
git add --all
git commit -m "chore: remove template examples and add site identity"
```

### Task 7: Build, Inspect, and Publish the Review Branch

**Files:**
- Generated and ignored: `_site/`
- Verify: built `index.html`, CSS, portrait, favicon, DOI links

- [ ] **Step 1: Verify DOI endpoints**

Run:

```powershell
$doiUrls = @(
  'https://doi.org/10.1145/3832194',
  'https://doi.org/10.1016/j.infsof.2025.107975',
  'https://doi.org/10.1016/j.eswa.2025.127470',
  'https://doi.org/10.11897/SP.J.1016.2024.00172',
  'https://doi.org/10.1109/COMPSAC57700.2023.00119'
)
foreach ($doiUrl in $doiUrls) { curl.exe --head --location --fail --max-time 30 $doiUrl }
```

Expected: each resolves to a publisher page without a 4xx or 5xx response. If a publisher blocks automated requests, query `https://api.crossref.org/works/<DOI>` and require a successful metadata response before retaining the CV wording.

- [ ] **Step 2: Build with the supported Jekyll environment**

If Docker is available, run:

```powershell
docker build -t shifan-academic-homepage .
docker run --rm -v "${PWD}:/usr/src/app" -w /usr/src/app shifan-academic-homepage bundle exec jekyll build --strict_front_matter
```

Expected: exit code 0 and `_site/index.html` exists. If the Docker daemon is unavailable, push the feature branch first and use the repository's `Jekyll build` GitHub Action as the build gate.

- [ ] **Step 3: Perform static output checks**

Run:

```powershell
rg -n "Shifan Liu|id=\"about\"|id=\"publications\"|id=\"education\"|10\.1145/3832194" _site/index.html
rg -n -g "*.html" "Your Name|John Snow|Research Experience|Honors|Awards|Download CV|theme-toggle" _site
```

Expected: the first command finds all required content; the second finds no visible placeholder or excluded content.

- [ ] **Step 4: Start a local preview and inspect desktop and mobile**

Run:

```powershell
$previewProcess = Start-Process -FilePath python -ArgumentList '-m','http.server','4000','--directory','_site' -WindowStyle Hidden -PassThru
```

Open `http://127.0.0.1:4000/` in the local preview browser. Inspect at the normal desktop viewport, then at 390 x 844. Confirm the portrait is centered on the face, the navigation anchors land below the sticky header, the white background remains white regardless of OS theme, publication and education rows do not overflow, focus states are visible, and no CV or research-experience content appears. Stop only this captured process after inspection with `Stop-Process -Id $previewProcess.Id`.

- [ ] **Step 5: Run final repository verification**

Run:

```powershell
python -m unittest discover -s tests -v
git diff --check
git status --short --branch
```

Expected: all tests pass, diff check is clean, and no generated `_site/` files or unrelated changes are staged.

- [ ] **Step 6: Push only the review branch**

Run:

```powershell
git push -u origin codex/academic-homepage
```

Expected: the feature branch is available in `rookieLiu2018/rookieLiu2018.github.io`. Do not merge or force-push `main` before the user reviews the finished preview.
