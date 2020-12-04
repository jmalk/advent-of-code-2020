import unittest
from expirationyear import is_valid_expiration_year


class TestIsValidExpirationYear(unittest.TestCase):
    def test_five_digits_invalid(self):
        self.assertEqual(is_valid_expiration_year("12345"), False,
                         "Should be False")

    def test_four_non_digits_invalid(self):
        self.assertEqual(is_valid_expiration_year("asdf"), False,
                         "Should be False")

    def test_small_number_invalid(self):
        self.assertEqual(is_valid_expiration_year("2019"), False,
                         "Should be False")

    def test_just_big_enough_valid(self):
        self.assertEqual(is_valid_expiration_year("2020"), True,
                         "Should be True")

    def test_just_small_enough_valid(self):
        self.assertEqual(is_valid_expiration_year("2030"), True,
                         "Should be True")

    def test_too_big_invalid(self):
        self.assertEqual(is_valid_expiration_year("2031"), False,
                         "Should be False")


if __name__ == '__main__':
    unittest.main()