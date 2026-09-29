"""Validation tests for reports.py (report output and grading logic)."""
import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reports import show_report, get_relative_grade_map, calculate_grade


class TestReports(unittest.TestCase):
    def test_calculate_grade_boundaries(self):
        cases = {90: "S", 89: "A", 80: "A", 79: "B", 70: "B", 60: "C",
                 50: "D", 40: "E", 39: "F", 0: "F"}
        for marks, expected in cases.items():
            self.assertEqual(calculate_grade(marks), expected)

    def test_relative_grades_follow_rank(self):
        students = [{"marks": "90"}, {"marks": "70"}, {"marks": "50"}]
        grade_map = get_relative_grade_map(students)
        self.assertEqual(grade_map, {90: "S", 70: "A", 50: "B"})

    def test_tied_marks_get_same_grade(self):
        students = [{"marks": "80"}, {"marks": "80"}, {"marks": "60"}]
        grade_map = get_relative_grade_map(students)
        self.assertEqual(grade_map[80], "S")
        self.assertEqual(grade_map[60], "A")

    def test_more_than_seven_unique_marks_cap_at_F(self):
        students = [{"marks": str(m)} for m in range(100, 90, -1)]  # 10 unique
        grade_map = get_relative_grade_map(students)
        self.assertEqual(grade_map[91], "F")

    def test_report_on_empty_list(self):
        with patch("sys.stdout", new=StringIO()) as out:
            show_report([])
        self.assertIn("No records found", out.getvalue())

    def test_report_average_and_topper(self):
        students = [
            {"roll": "1", "name": "Asha", "marks": "80"},
            {"roll": "2", "name": "Ravi", "marks": "60"},
        ]
        with patch("sys.stdout", new=StringIO()) as out:
            show_report(students)
        text = out.getvalue()
        self.assertIn("Average marks: 70.0", text)
        self.assertIn("Name: Asha", text)


if __name__ == "__main__":
    unittest.main()
