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


if __name__ == '__main__':
    unittest.main()
