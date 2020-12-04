import unittest
from haircolor import is_valid_hair_color


class TestIsValidHairColor(unittest.TestCase):
    def test_valid_hair_color(self):
        self.assertEqual(is_valid_hair_color("#abf123"), True,
                         "Should be True")

    def test_no_hash_is_invalid(self):
        self.assertEqual(is_valid_hair_color("abf123"), False,
                         "Should be False")

    def test_hash_not_at_start_is_invalid(self):
        self.assertEqual(is_valid_hair_color("abf#123"), False,
                         "Should be False")

    def test_too_many_characters(self):
        self.assertEqual(is_valid_hair_color('#1234567'), False,
                         "Should be False")

    def test_too_few_characters(self):
        self.assertEqual(is_valid_hair_color('#12345'), False,
                         "Should be False")

    def test_non_hexadecimal_characters(self):
        self.assertEqual(is_valid_hair_color('#ghijkl'), False,
                         "Should be False")


if __name__ == '__main__':
    unittest.main()