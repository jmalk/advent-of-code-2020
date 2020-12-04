import unittest
from eyecolor import is_valid_eye_color


class TestIsValidEyeColor(unittest.TestCase):
    def test_valid_eye_colors(self):
        valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        for color in valid:
            self.assertEqual(is_valid_eye_color(color), True, "Should be True")

    def test_invalid_eye_color(self):
        self.assertEqual(is_valid_eye_color('blugrn'), False,
                         "Should be False")


if __name__ == '__main__':
    unittest.main()