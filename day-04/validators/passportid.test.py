import unittest
from passportid import is_valid_passport_id


class TestIsValidPassportId(unittest.TestCase):
    def test_valid_passport_id(self):
        self.assertEqual(is_valid_passport_id("012345678"), True,
                         "Should be True")

    def test_letters_invalid(self):
        self.assertEqual(is_valid_passport_id("abcdefghi"), False,
                         "Should be False")

    def test_too_short(self):
        self.assertEqual(is_valid_passport_id("01234567"), False,
                         "Should be False")

    def test_too_long(self):
        self.assertEqual(is_valid_passport_id("0123456789"), False,
                         "Should be False")

    def test_one_non_digit_invalid(self):
        self.assertEqual(is_valid_passport_id("a12345678"), False,
                         "Should be False")


if __name__ == '__main__':
    unittest.main()