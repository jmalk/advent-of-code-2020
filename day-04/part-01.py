"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID) - optional!
"""

from validators.birthyear import is_valid_birth_year
from validators.issueyear import is_valid_issue_year
from validators.expirationyear import is_valid_expiration_year
from validators.height import is_valid_height
from validators.haircolor import is_valid_hair_color
from validators.eyecolor import is_valid_eye_color
from validators.passportid import is_valid_passport_id

with open('input.txt', 'r') as f:
    file_string = ''.join(f.readlines())
f.close()

# Passports are separated by a blank line
passports = file_string.split("\n\n")

# There are sometimes newline characters within a single passport entry
# Make each key-value pair space-separated.
passports = [pp.replace("\n", " ") for pp in passports]


def to_dict(passport_string):
    as_list = passport_string.split(' ')
    as_key_values = [pair.split(':') for pair in as_list]
    as_dict = dict(as_key_values)
    return as_dict


passport_dicts = [to_dict(pp) for pp in passports]


def has_all_fields(passport):
    return "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport


def count_has_all_fields(passports):
    total = 0
    for passport in passports:
        if has_all_fields(passport):
            total += 1
    return total


def is_valid(passport):
    all_fields = has_all_fields(passport)

    if all_fields:
        byr = is_valid_birth_year(passport['byr'])
        iyr = is_valid_issue_year(passport['iyr'])
        eyr = is_valid_expiration_year(passport['eyr'])
        hgt = is_valid_height(passport['hgt'])
        hcl = is_valid_hair_color(passport['hcl'])
        ecl = is_valid_eye_color(passport['ecl'])
        pid = is_valid_passport_id(passport['pid'])
        return byr and iyr and eyr and hgt and hcl and ecl and pid
    return False


def count_valid(passports):
    total = 0
    for passport in passports:
        if is_valid(passport):
            total += 1
    return total


print('Part 1: ', count_has_all_fields(passport_dicts))  # 230
print('Part 2: ', count_valid(passport_dicts))
