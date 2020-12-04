import re


# Could use number in range(x, y)
# but don't like the (inclusive, exclusive) thing for this use case.
def is_in_inclusive_range(number, minimum, maximum):
    return minimum <= number <= maximum


def is_four_digits(string):
    return re.match(r'\d{4}$', string) != None


def is_valid_expiration_year(birth_year):
    return is_four_digits(birth_year) and is_in_inclusive_range(
        int(birth_year), 2020, 2030)
