import unittest
from height import is_valid_height


class TestIsValidHeight(unittest.TestCase):
    """
    Heights in centimetres
    """
    def test_too_small_cm(self):
        self.assertEqual(is_valid_height("149cm"), False, "Should be False")

    def test_too_big_cm(self):
        self.assertEqual(is_valid_height("194cm"), False, "Should be False")

    def test_all_valid_cm(self):
        for number in range(150, 193 + 1):
            self.assertEqual(is_valid_height(str(number) + 'cm'), True,
                             "Should be True")

    def test_no_cm_invalid(self):
        self.assertEqual(is_valid_height("160"), False, "Should be False")

    """
    Heights in inches
    """

    def test_too_small_inches(self):
        self.assertEqual(is_valid_height("58in"), False, "Should be False")

    def test_too_big_inches(self):
        self.assertEqual(is_valid_height("77in"), False, "Should be False")

    def test_all_valid_inches(self):
        for number in range(59, 76 + 1):
            self.assertEqual(is_valid_height(str(number) + 'in'), True,
                             "Should be True")

    def test_no_inches_invalid(self):
        self.assertEqual(is_valid_height("65"), False, "Should be False")


if __name__ == '__main__':
    unittest.main()