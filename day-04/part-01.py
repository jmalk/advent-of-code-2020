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


def is_valid(passport):
    return "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport


def count_valid(passports):
    total = 0
    for passport in passports:
        if is_valid(passport):
            total += 1
    return total


print(count_valid(passport_dicts))  # 230
