from functools import reduce

with open('input.txt', 'r') as f:
    lines = f.readlines()
f.close()

lines = [l.replace("\n", "") for l in lines]

slope = [list(line) for line in lines]

TREE = '#'


def traverse_slope(slope, delta_x, delta_y):
    # Returns how many trees encountered while travelling across slope.
    # Travel is done in steps, where each step changes current position by delta_x, delta_y.

    trees_encountered = 0

    # Starting position 0,0 (top left)
    toboggan_x = 0
    toboggan_y = 0

    slope_height = len(slope)
    slope_width = len(slope[0])  # assuming all rows are same length

    while toboggan_y < slope_height:
        # Take modulus because map repeats infinitely in x-direction
        effective_x = toboggan_x % slope_width

        if slope[toboggan_y][effective_x] == TREE:
            trees_encountered = trees_encountered + 1

        toboggan_x = toboggan_x + delta_x
        toboggan_y = toboggan_y + delta_y

    return trees_encountered


class Route:
    def __init__(self, gradient_x, gradient_y):
        self.gradient_x = gradient_x
        self.gradient_y = gradient_y


routes = [Route(1, 1), Route(3, 1), Route(5, 1), Route(7, 1), Route(1, 2)]

trees_per_route = [
    traverse_slope(slope, route.gradient_x, route.gradient_y)
    for route in routes
]

total = reduce((lambda a, b: a * b), trees_per_route)

print('Part 1: ', traverse_slope(slope, 3, 1))
print('Part 2: ', total)
