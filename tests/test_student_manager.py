"""Validation tests for student_manager.py (add, view, search, delete)."""
import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student_manager import add_student, view_students, search_student, delete_student


def capture(func, *args):
    """Run func and return everything it printed."""
    with patch("sys.stdout", new=StringIO()) as out:
        func(*args)
    return out.getvalue()


class TestStudentManager(unittest.TestCase):
    def test_add_student_appends_record(self):
        students = []
        with patch("builtins.input", side_effect=["1", "Asha", "88"]):
            capture(add_student, students)
        self.assertEqual(students, [{"roll": "1", "name": "Asha", "marks": "88"}])

    def test_view_empty_list(self):
        self.assertIn("No records found", capture(view_students, []))

    def test_view_shows_record_and_grade(self):
        students = [{"roll": "1", "name": "Asha", "marks": "88"}]
        output = capture(view_students, students)
        self.assertIn("Asha", output)
        self.assertIn("Grade: A", output)

    def test_search_found(self):
        students = [{"roll": "1", "name": "Asha", "marks": "88"}]
        with patch("builtins.input", return_value="1"):
            output = capture(search_student, students)
        self.assertIn("Student found", output)

    def test_search_not_found(self):
        students = [{"roll": "1", "name": "Asha", "marks": "88"}]
        with patch("builtins.input", return_value="99"):
            output = capture(search_student, students)
        self.assertIn("No student found", output)

    def test_delete_existing(self):
        students = [{"roll": "1", "name": "Asha", "marks": "88"}]
        with patch("builtins.input", return_value="1"):
            output = capture(delete_student, students)
        self.assertEqual(students, [])
        self.assertIn("deleted successfully", output)

    def test_delete_missing_leaves_list_unchanged(self):
        students = [{"roll": "1", "name": "Asha", "marks": "88"}]
        with patch("builtins.input", return_value="99"):
            output = capture(delete_student, students)
        self.assertEqual(len(students), 1)
        self.assertIn("No student found", output)


if __name__ == "__main__":
    unittest.main()
