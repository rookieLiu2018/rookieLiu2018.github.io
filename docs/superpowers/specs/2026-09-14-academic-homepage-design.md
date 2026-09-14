# Shifan Liu Academic Homepage Design

## Goal

Replace the current placeholder-style personal site with a polished, English-language academic homepage based on the widely used Academic Pages template. The site should present Shifan Liu's research identity, selected publications, research experience, education, and downloadable CV clearly to academic visitors.

## Source and Delivery Strategy

- Use `academicpages/academicpages.github.io` as the upstream design and content structure.
- Create a GitHub fork under `rookieLiu2018` to preserve upstream provenance.
- Adapt the template content for the existing public site repository, `rookieLiu2018/rookieLiu2018.github.io`.
- Perform all changes on the `codex/academic-homepage` branch first. Do not replace the published `main` branch until the customized site has been built and reviewed.
- Preserve the previous site through Git history; do not delete or rewrite repository history.

## Audience and Primary Task

The primary audience is researchers, conference attendees, prospective collaborators, and academic evaluators. A visitor should be able to understand the research focus, inspect representative work, verify publications through DOI links, and download the CV with minimal navigation.

## Information Architecture

The first version will contain five primary destinations:

1. **About** - name, current role, affiliation, contact information, concise research profile, and research interests.
2. **Research** - three focused research themes drawn from the CV: historical-bug-driven testing of deep learning frameworks, transfer testing of deep learning compilers, and AI-assisted software maintenance and evolution.
3. **Publications** - five selected publications with complete author lists, venues, years, and DOI links.
4. **Experience** - research experience and education in a concise chronological presentation.
5. **CV** - a direct link to the supplied PDF, stored as a downloadable site asset.

Awards and honors are explicitly out of scope for this version because no verified award information was provided. Blog posts, teaching pages, talks, analytics, and contact forms are also out of scope.

## Content Source of Truth

The supplied PDF at `E:\data-Processing\AScI_Application_Shifan_Liu_2026\01_CV.pdf` is the source of truth for biography, research interests, education, research experience, publications, email address, and affiliation. Content may be shortened for web readability but must not introduce unsupported claims or metrics.

The publication list will include:

1. SpectraDL, ISSTA 2026, DOI `10.1145/3832194`.
2. CPMT, Information and Software Technology, 2026, DOI `10.1016/j.infsof.2025.107975`.
3. SEOCD, Expert Systems with Applications, 2025, DOI `10.1016/j.eswa.2025.127470`.
4. MMCUP, Chinese Journal of Computers, 2024, DOI `10.11897/SP.J.1016.2024.00172`.
5. TBCUP, COMPSAC 2023, DOI `10.1109/COMPSAC57700.2023.00119`.

## Visual Direction

Use a single light theme with a white background. The visual language should be restrained, precise, and academic:

- deep navy for headings and active navigation;
- near-black body text and cool gray metadata;
- thin neutral dividers and minimal borders;
- generous whitespace and a readable editorial measure;
- compact publication cards or list items with clear venue and year hierarchy;
- no gradients, decorative hero artwork, dark mode, or oversized marketing-style hero section.

The supplied CV portrait and all other personal photographs must not appear on the site. The identity area should rely on typography and concise research positioning instead.

## Responsive and Accessibility Behavior

- Preserve a clear navigation path on desktop and mobile.
- Keep body text at a comfortable reading size and avoid horizontal scrolling.
- Use semantic headings, lists, links, and navigation landmarks.
- Ensure keyboard-visible focus states and sufficient text/link contrast on white.
- Give DOI and CV links descriptive accessible labels.

## Content and Data Flow

Site-wide identity and contact information will live in the template configuration. Long-form overview content will live in Markdown pages. Publications will use the template's structured publication format so author, venue, year, and DOI presentation remain consistent. The CV PDF will be copied unchanged into the site's public files directory and linked from both navigation and the About page.

## Failure Handling

- If the fork name conflicts with an existing repository, keep the fork under an available explicit name and continue using it as the upstream source.
- If a DOI cannot be resolved during verification, preserve the DOI text from the CV but do not claim that the link was verified.
- If the GitHub Pages build fails, fix configuration or dependency compatibility on the feature branch before proposing publication.
- Do not publish placeholder content, template example people, example publications, or broken social links.

## Verification

- Build the Jekyll site successfully using the template-supported workflow.
- Check the homepage, Research, Publications, Experience, and CV link.
- Confirm all visible biographical claims against the supplied CV.
- Verify the five DOI links and the downloadable CV asset.
- Inspect desktop and mobile layouts for clipping, overflow, hierarchy, contrast, and accidental dark-mode behavior.
- Confirm there are no remaining template names, sample posts, sample social accounts, or personal photos.

## Acceptance Criteria

The design is complete when the feature branch contains a buildable Academic Pages-based site that uses a white-only theme, contains only verified CV-derived academic content, shows the five selected publications and three research themes, provides the CV download, contains no portrait or Awards section, and is ready for the user's review before updating the published branch.
