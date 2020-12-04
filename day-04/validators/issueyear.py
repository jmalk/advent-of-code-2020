import re


def is_four_digits(string):
    return re.match(r'\d{4}$', string) != None


def is_valid_issue_year(birth_year):
    return is_four_digits(birth_year) and 2010 <= int(birth_year) <= 2020
