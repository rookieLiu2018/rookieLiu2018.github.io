# Shifan Liu Academic Homepage Design

## Goal

Replace the current placeholder-style personal site with a polished, English-language academic homepage based on the widely used Academic Pages template. The site should present Shifan Liu's research identity, selected publications, and education clearly to academic visitors.

## Source and Delivery Strategy

- Use `academicpages/academicpages.github.io` as the upstream design and content structure.
- Create a GitHub fork under `rookieLiu2018` to preserve upstream provenance.
- Adapt the template content for the existing public site repository, `rookieLiu2018/rookieLiu2018.github.io`.
- Perform all changes on the `codex/academic-homepage` branch first. Do not replace the published `main` branch until the customized site has been built and reviewed.
- Preserve the previous site through Git history; do not delete or rewrite repository history.

## Audience and Primary Task

The primary audience is researchers, conference attendees, prospective collaborators, and academic evaluators. A visitor should be able to understand the research focus and verify representative publications through DOI links with minimal navigation.

## Information Architecture

The first version will use one compact homepage with three anchored sections:

1. **About** - name, current role, affiliation, contact information, concise research profile, and research interests.
2. **Publications** - five selected publications with complete author lists, venues, years, and DOI links.
3. **Education** - the three verified degree entries in a concise chronological presentation.

The top navigation will link to these homepage anchors instead of sending visitors through separate content pages. Publication titles may link directly to DOI landing pages.

Research experience, downloadable CV files, awards and honors, blog posts, teaching pages, talks, analytics, and contact forms are explicitly out of scope for this version.

## Content Source of Truth

The supplied PDF at `E:\data-Processing\AScI_Application_Shifan_Liu_2026\01_CV.pdf` is the source of truth for biography, research interests, education, publications, email address, and affiliation. It is an input reference only and must not be copied into the public site. Content may be shortened for web readability but must not introduce unsupported claims or metrics.

The publication list will include:

1. SpectraDL, ISSTA 2026, DOI `10.1145/3832194`.
2. CPMT, Information and Software Technology, 2026, DOI `10.1016/j.infsof.2025.107975`.
3. SEOCD, Expert Systems with Applications, 2025, DOI `10.1016/j.eswa.2025.127470`.
4. MMCUP, Chinese Journal of Computers, 2024, DOI `10.11897/SP.J.1016.2024.00172`.
5. TBCUP, COMPSAC 2023, DOI `10.1109/COMPSAC57700.2023.00119`.

## Visual Direction

Use `https://samxrl.github.io/` as the visual reference for overall information density and hierarchy: a compact top navigation, a left identity sidebar, and a broad main reading column with section anchors. Reproduce the general academic-homepage character without copying its wording or assets.

Use a single light theme with a white background. The visual language should be restrained, precise, and academic:

- deep navy for headings and active navigation;
- near-black body text and cool gray metadata;
- thin neutral dividers and minimal borders;
- generous whitespace and a readable editorial measure;
- a compact portrait in the left identity sidebar on desktop, moving above the content on narrow screens;
- compact publication cards or list items with clear venue and year hierarchy;
- no gradients, decorative hero artwork, dark mode, or oversized marketing-style hero section.

Use the user-supplied photograph `C:\Users\liu\AppData\Local\Temp\codex-clipboard-bacc5d6d-c22a-4a5e-9696-a39e0fb5875f.jpg` as the profile portrait. Present it with a centered face-aware crop using layout styling; do not use the portrait embedded in the CV. Do not apply generative edits or materially alter the photograph.

## Responsive and Accessibility Behavior

- Preserve a clear navigation path on desktop and mobile.
- Keep body text at a comfortable reading size and avoid horizontal scrolling.
- Use semantic headings, lists, links, and navigation landmarks.
- Ensure keyboard-visible focus states and sufficient text/link contrast on white.
- Give DOI links descriptive accessible labels.

## Content and Data Flow

Site-wide identity and contact information will live in the template configuration. The homepage Markdown will own the About, Publications, and Education sections so the full academic profile can be scanned without page changes. The source CV will remain outside the repository and will not be linked or published.

## Failure Handling

- If the fork name conflicts with an existing repository, keep the fork under an available explicit name and continue using it as the upstream source.
- If a DOI cannot be resolved during verification, preserve the DOI text from the CV but do not claim that the link was verified.
- If the GitHub Pages build fails, fix configuration or dependency compatibility on the feature branch before proposing publication.
- Do not publish placeholder content, template example people, example publications, or broken social links.

## Verification

- Build the Jekyll site successfully using the template-supported workflow.
- Check the About, Publications, and Education anchors on the homepage.
- Confirm all visible biographical claims against the supplied CV.
- Verify the five DOI links.
- Inspect desktop and mobile layouts for clipping, overflow, hierarchy, contrast, and accidental dark-mode behavior.
- Confirm there are no remaining template names, sample posts, sample social accounts, or photographs other than the user-supplied profile portrait.

## Acceptance Criteria

The design is complete when the feature branch contains a buildable Academic Pages-based site that follows the compact sidebar-and-content character of the approved visual reference, uses a white-only theme, includes the user-supplied profile portrait, contains only verified CV-derived academic content, shows a concise research profile, research interests, education, and the five selected publications, contains no research-experience section, CV download, or Awards section, and is ready for the user's review before updating the published branch.
