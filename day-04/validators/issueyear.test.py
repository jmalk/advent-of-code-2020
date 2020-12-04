import unittest
from issueyear import is_valid_issue_year


class TestIsValidIssueYear(unittest.TestCase):
    def test_five_digits_invalid(self):
        self.assertEqual(is_valid_issue_year("12345"), False,
                         "Should be False")

    def test_four_non_digits_invalid(self):
        self.assertEqual(is_valid_issue_year("asdf"), False, "Should be False")

    def test_small_number_invalid(self):
        self.assertEqual(is_valid_issue_year("2009"), False, "Should be False")

    def test_just_big_enough_valid(self):
        self.assertEqual(is_valid_issue_year("2010"), True, "Should be True")

    def test_just_small_enough_valid(self):
        self.assertEqual(is_valid_issue_year("2020"), True, "Should be True")

    def test_too_big_invalid(self):
        self.assertEqual(is_valid_issue_year("2021"), False, "Should be False")


if __name__ == '__main__':
    unittest.main()