"""Validation tests for file_handler.py (save/load persistence)."""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from file_handler import save_students, load_students


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        # file_handler uses a relative path, so run each test in a temp folder
        self.original_dir = os.getcwd()
        self.temp = tempfile.TemporaryDirectory()
        os.chdir(self.temp.name)

    def tearDown(self):
        os.chdir(self.original_dir)
        self.temp.cleanup()

    def test_load_returns_empty_list_when_file_missing(self):
        self.assertEqual(load_students(), [])

    def test_save_then_load_round_trip(self):
        students = [
            {"roll": "1", "name": "Asha", "marks": "88"},
            {"roll": "2", "name": "Ravi", "marks": "67"},
        ]
        save_students(students)
        self.assertEqual(load_students(), students)

    def test_save_empty_list_creates_empty_file(self):
        save_students([])
        self.assertTrue(os.path.exists("students.txt"))
        self.assertEqual(load_students(), [])


if __name__ == "__main__":
    unittest.main()
