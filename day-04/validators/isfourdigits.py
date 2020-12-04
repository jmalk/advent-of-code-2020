import re


def is_four_digits(string):
    return re.match(r'\d{4}$', string) != None