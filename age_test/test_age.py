import unittest
from age import categorize_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_child(self):
        self.assertEqual(categorize_by_age(5), "Child")
        self.assertEqual(categorize_by_age(12), "Child")

    def test_teenager(self):
        self.assertEqual(categorize_by_age(18), "Teenager")

    def test_adult(self):
        self.assertEqual(categorize_by_age(20), "Adult")
        self.assertEqual(categorize_by_age(64), "Adult")

    def test_senior(self):
        self.assertEqual(categorize_by_age(65), "Senior")
        self.assertEqual(categorize_by_age(80), "Senior")

    def test_invalid_age(self):
        self.assertEqual(categorize_by_age(-1), "Invalid age")

    def test_invalid_age(self):
        self.assertEqual(categorize_by_age(-5), "Invalid age")  
        self.assertEqual(categorize_by_age(-1), "Invalid age")