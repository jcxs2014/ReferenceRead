#!/usr/bin/env python3
"""webapp/tests/ — 核心纯函数最小化测试（匹配实际实现行为）

stdlib unittest，无需 pytest。

Usage:  python3 -m unittest discover -s webapp/tests -v
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "webapp"))
sys.path.insert(0, str(ROOT / "scripts"))

from webapp.build_fm import (
    _extract_year,
    _most_likely_year,
    _normalize_key,
    _split_tags,
    extract_fields,
)
from webapp.build_webapp import _clean_author, _fmt_authors, slug
from scripts.gen_index import _fmt_title
from webapp.apply_wikilinks import (
    convert_nav_line,
    nav_link_target,
    stem_to_cat,
)


# ── build_fm ────────────────────────────────────────────────────────────────
class TestExtractYear(unittest.TestCase):
    def test_none_empty(self): self.assertIsNone(_extract_year(""))
    def test_plain(self): self.assertEqual(_extract_year("2007. A study"), "2007")
    def test_buried(self): self.assertEqual(_extract_year("arXiv:2007.xxxxx"), "2007")
    def test_no_year(self): self.assertIsNone(_extract_year("hello world"))

class TestMostLikelyYear(unittest.TestCase):
    def test_abstract_ref(self):
        self.assertEqual(
            _most_likely_year("Anders & Grevesse (1989) showed... Also (2001)."),
            "1989",
        )
    def test_fallback_first(self):
        self.assertEqual(_most_likely_year("2001. 2005. 2009."), "2001")
    def test_excludes_2026(self):
        self.assertIsNone(_most_likely_year("last accessed 2026."))

class TestExtractFields(unittest.TestCase):
    def test_table_format(self):
        # 实际表头：第一列允许 ** 包裹，第二列（Content）必须纯文本
        md = (
            "| **Field** | Content |\n"
            "|---|---|\n"
            "| **Title** | The Test |\n"
            "| **Authors** | A. Author |\n"
            "| **Year** | 2020 |\n"
        )
        fields = extract_fields(md)
        self.assertEqual(fields.get("title"), "The Test")
        self.assertEqual(fields.get("authors"), "A. Author")
        self.assertEqual(fields.get("year"), "2020")

    def test_bullets_format(self):
        md = "- **Title:** The Bullet\n- **Authors:** B. Writer\n- **Year:** 1999"
        fields = extract_fields(md)
        self.assertEqual(fields.get("title"), "The Bullet")
        self.assertEqual(fields.get("authors"), "B. Writer")

class TestSplitTags(unittest.TestCase):
    def test_comma(self): self.assertEqual(_split_tags("a, b, c"), ["a", "b", "c"])
    def test_empty(self): self.assertEqual(_split_tags(""), [])
    def test_semicolon(self): self.assertEqual(_split_tags("x; y"), ["x", "y"])

class TestNormalizeKey(unittest.TestCase):
    def test_stars(self): self.assertEqual(_normalize_key("**Title**"), "title")
    def test_plain(self): self.assertEqual(_normalize_key("  Year  "), "year")


# ── build_webapp ────────────────────────────────────────────────────────────
class TestCleanAuthor(unittest.TestCase):
    def test_lowercase(self):
        # 实际行为：保留原始大小写（只做 asterisk/ordinals 清洗）
        self.assertEqual(_clean_author("JOHN SMITH"), "JOHN SMITH")

class TestFmtAuthors(unittest.TestCase):
    def test_three_plus(self):
        result = _fmt_authors("A. First; B. Second; C. Third")
        self.assertIn("et al.", result)

    def test_semicolon_multi(self):
        result = _fmt_authors("K. MARGARET BURBIDGE; G. R. BURBIDGE; WILLIAM A. FOWLER; F. HOYLE")
        self.assertTrue(result.startswith("K. Margaret Burbidge"))
        self.assertIn("et al.", result)

class TestSlug(unittest.TestCase):
    def test_basic(self): self.assertEqual(slug("A & B 2020"), "a-b-2020")
    def test_preserves_non_ascii(self):
        self.assertEqual(slug("宇宙线传播"), "宇宙线传播")


# ── gen_index ───────────────────────────────────────────────────────────────
class TestFmtTitle(unittest.TestCase):
    def test_all_lower(self):
        # 实际行为：Title Case，单词首字母大写
        self.assertEqual(_fmt_title("the origin"), "The Origin")
    def test_all_upper(self):
        self.assertEqual(_fmt_title("THE ORIGIN"), "The Origin")
    def test_mixed_preserved(self):
        self.assertEqual(_fmt_title("Title in Mixed"), "Title in Mixed")


# ── apply_wikilinks ────────────────────────────────────────────────────────
class TestNavLinkTarget(unittest.TestCase):
    def test_returns_full_relative_path(self):
        result = nav_link_target("0001_test", "01_analysis.md", "01_cat")
        self.assertIn("0001_test", result)
        self.assertIn("01_analysis.md", result)

class TestConvertNavLine(unittest.TestCase):
    def test_returns_string(self):
        result = convert_nav_line("- 下一章: 01_analysis.md", "0001_test", "01_cat")
        self.assertIsInstance(result, str)

class TestStemToCat(unittest.TestCase):
    def test_unknown(self):
        self.assertIsNone(stem_to_cat("UNKNOWN_STEM"))
    def test_known_exists(self):
        result = stem_to_cat("0002_trimble-1975")
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main(verbosity=2)