"""Small standard-library tests for the installable MCP package."""

import sys
import unittest
from pathlib import Path

PACKAGE_SOURCE = Path(__file__).resolve().parents[1] / "mcp_pypi_demo" / "src"
sys.path.insert(0, str(PACKAGE_SOURCE))

from mcp_pypi_demo.logic import process_text  # noqa: E402


class PackageToolTests(unittest.TestCase):
    def test_process_text_returns_a_summary_and_word_count(self) -> None:
        self.assertEqual(
            process_text("MCP tools are reusable and easy to test."),
            {"summary": "MCP tools are reusable and easy to test.", "word_count": 8},
        )

    def test_process_text_rejects_empty_input(self) -> None:
        with self.assertRaises(ValueError):
            process_text("   ")


if __name__ == "__main__":
    unittest.main()
