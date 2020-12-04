import re
from isfourdigits import is_four_digits
from isininclusiverange import is_in_inclusive_range


def is_valid_expiration_year(birth_year):
    return is_four_digits(birth_year) and is_in_inclusive_range(
        int(birth_year), 2020, 2030)
