import re


def is_valid_birth_year(birth_year):
    return re.match(r'\d{4}$', birth_year) != None and int(
        birth_year) >= 1920 and int(birth_year) <= 2020
