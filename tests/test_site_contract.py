import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class AcademicHomepageContract(unittest.TestCase):
    def test_identity_and_navigation(self):
        config = read("_config.yml")
        self.assertRegex(config, r'(?m)^title\s*:\s*["\']?Shifan Liu["\']?\s*$')
        self.assertRegex(
            config,
            r'(?m)^repository\s*:\s*["\']?rookieLiu2018/rookieLiu2018\.github\.io["\']?\s*$',
        )
        self.assertRegex(config, r'(?m)^\s*avatar\s*:\s*["\']?profile\.jpg["\']?\s*$')
        self.assertRegex(config, r'(?m)^\s*github\s*:\s*["\']?rookieLiu2018["\']?\s*$')

        navigation = read("_data/navigation.yml")
        self.assertIn("/#about", navigation)
        self.assertIn("/#publications", navigation)
        self.assertIn("/#education", navigation)
        self.assertNotIn("/cv/", navigation.lower())

    def test_homepage_contains_only_approved_sections(self):
        homepage = read("_pages/about.md")
        self.assertIn('id="about"', homepage)
        self.assertIn('id="publications"', homepage)
        self.assertIn('id="education"', homepage)
        self.assertIn("10.1145/3832194", homepage)
        self.assertIn("10.1016/j.infsof.2025.107975", homepage)
        self.assertIn("10.1016/j.eswa.2025.127470", homepage)
        self.assertIn("10.11897/SP.J.1016.2024.00172", homepage)
        self.assertIn("10.1109/COMPSAC57700.2023.00119", homepage)
        self.assertNotIn("Research Experience", homepage)
        self.assertNotIn("Awards", homepage)
        self.assertNotIn("Honors", homepage)
        self.assertNotIn("Download CV", homepage)

    def test_portrait_and_light_theme(self):
        portrait = ROOT / "images" / "profile.jpg"
        self.assertTrue(portrait.exists())
        self.assertGreater(portrait.stat().st_size, 100000)
        self.assertNotIn("append: '_dark'", read("assets/css/main.scss"))
        self.assertNotIn('id="theme-toggle"', read("_includes/masthead.html"))
        self.assertIn("--global-bg-color", read("_sass/theme/_default_light.scss"))
        self.assertIn("background: #fff", read("_sass/_custom.scss"))

    def test_example_content_is_removed(self):
        for dirname in ("_posts", "_talks", "_teaching", "_portfolio", "_publications"):
            with self.subTest(directory=dirname):
                path = ROOT / dirname
                self.assertTrue(not path.exists() or not any(path.iterdir()), dirname)
        self.assertFalse((ROOT / "_pages" / "cv.md").exists())
        self.assertFalse((ROOT / "_pages" / "publications.html").exists())

    def test_dormant_cv_and_collection_configuration_is_removed(self):
        removed_paths = (
            "scripts/update_cv_json.sh",
            "scripts/cv_markdown_to_json.py",
            "_data/cv.json",
            "_data/authors.yml",
            "_includes/cv-template.html",
            "_layouts/cv-layout.html",
            "_layouts/json_cv",
            "_sass/layout/_json_cv.scss",
        )
        for path in removed_paths:
            with self.subTest(path=path):
                self.assertFalse((ROOT / path).exists(), path)

        config = read("_config.yml")
        self.assertNotRegex(config, r"(?m)^\s*-\s*files\s*$")
        self.assertNotRegex(
            config,
            r"(?m)^\s{2}(?:teaching|publications|portfolio|talks):\s*$",
        )
        self.assertNotRegex(
            config,
            r"(?m)^\s+type:\s*(?:teaching|publications|portfolio|talks)\s*$",
        )
        self.assertNotRegex(config, r"(?m)^(?:category|tag)_archive:\s*$")
        self.assertNotIn('"layout/json_cv"', read("assets/css/main.scss"))

    def test_build_output_is_locally_reviewable_and_excludes_internal_files(self):
        base_path = read("_includes/base_path")
        self.assertIn("assign base_path = site.baseurl", base_path)
        self.assertNotIn("site.url | append: site.baseurl", base_path)

        config = read("_config.yml")
        for path in ("docs", "tests", "scripts", "AGENTS.md", "docker-compose.yaml"):
            with self.subTest(path=path):
                self.assertRegex(config, rf'(?m)^\s*-\s*["\']?{path}["\']?\s*$')

    def test_sitemap_and_ci_do_not_publish_unverified_content(self):
        sitemap = read("_pages/sitemap.md")
        self.assertIn("post.title | strip", sitemap)
        self.assertIn('page_title != ""', sitemap)

        workflow = read(".github/workflows/jekyll-build.yml")
        contract_command = "python -m unittest discover -s tests -v"
        self.assertIn(contract_command, workflow)
        self.assertLess(workflow.index(contract_command), workflow.index("- name: Build site"))


if __name__ == '__main__':
    unittest.main()
