# Could use number in range(x, y)
# but don't like the (inclusive, exclusive) thing for this use case.


def is_in_inclusive_range(number, minimum, maximum):
    return minimum <= number <= maximum