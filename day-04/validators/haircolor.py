import re


def is_valid_hair_color(string):
    return re.match(r'#[a-f\d]{6}$', string) != None