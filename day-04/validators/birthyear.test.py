import unittest

from birthyear import is_valid_birth_year


class TestSum(unittest.TestCase):
    def test_five_digits_invalid(self):
        self.assertEqual(is_valid_birth_year("12345"), False,
                         "Should be False")

    def test_four_non_digits_invalid(self):
        self.assertEqual(is_valid_birth_year("asdf"), False, "Should be False")

    def test_small_number_invalid(self):
        self.assertEqual(is_valid_birth_year("1919"), False, "Should be False")

    def test_just_big_enough_valid(self):
        self.assertEqual(is_valid_birth_year("1920"), True, "Should be True")

    def test_just_small_enough_valid(self):
        self.assertEqual(is_valid_birth_year("2020"), True, "Should be True")

    def test_too_big_invalid(self):
        self.assertEqual(is_valid_birth_year("2021"), False, "Should be False")


if __name__ == '__main__':
    unittest.main()