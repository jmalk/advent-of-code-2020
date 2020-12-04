# Could use number in range(x, y)
# but don't like the (inclusive, exclusive) thing for this use case.
def is_in_inclusive_range(number, minimum, maximum):
    return minimum <= number <= maximum


def is_valid_height_cm(string):
    no_cm = string[:-2]
    number_no_cm = int(no_cm)
    return is_in_inclusive_range(number_no_cm, 150, 193)


def is_valid_height_inches(string):
    no_in = string[:-2]
    number_no_in = int(no_in)
    return is_in_inclusive_range(number_no_in, 59, 76)


def is_valid_height(string):
    if string.endswith('cm'):
        return is_valid_height_cm(string)
    elif string.endswith('in'):
        return is_valid_height_inches(string)
    else:
        return False