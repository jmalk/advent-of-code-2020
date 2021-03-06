with open('sample-input.txt') as f:
    sample_lines = f.read().splitlines()
f.close()

with open('input.txt') as f:
    lines = f.read().splitlines()
f.close()

ACTIVE = '#'
INACTIVE = '.'

sample_active_cells = []
active_cells = []

for y in range(0, len(sample_lines)):
    for x in range(0, len(sample_lines[y])):
        if sample_lines[y][x] == ACTIVE:
            sample_active_cells.append((x, y, 0))

for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        if lines[y][x] == ACTIVE:
            active_cells.append((x, y, 0))


def same_coord(coord_a, coord_b):
    a_x, a_y, a_z = coord_a
    b_x, b_y, b_z = coord_b
    return a_x == b_x and a_y == b_y and a_z == b_z


def count_neighbours(coord, active_cells):
    cell_x = coord[0]
    cell_y = coord[1]
    cell_z = coord[2]

    n_neighbours = 0

    # +2 because ranges are inclusive, exclusive.
    for x in range(cell_x - 1, cell_x + 2):
        for y in range(cell_y - 1, cell_y + 2):
            for z in range(cell_z - 1, cell_z + 2):
                if not (same_coord((cell_x, cell_y, cell_z), (x, y, z))):
                    if ((x, y, z) in active_cells):
                        n_neighbours += 1
    return n_neighbours


# Don't count yourself
assert count_neighbours((0, 0, 0), [(0, 0, 0)]) == 0
# Do count a neighbour
assert count_neighbours((1, 1, 1), [(2, 1, 1)]) == 1
# Do count a diagonal neighbour
assert count_neighbours((0, 0, 0), [(1, 0, 0), (1, 1, 1)]) == 2
# Do count neighbours in negative half of axes
assert count_neighbours((0, 0, 0), [(-1, -1, -1)]) == 1
# Don't count duplicates
assert count_neighbours((0, 0, 0), [(1, 0, 0), (1, 1, 1), (1, 1, 1)]) == 2


# Only need to consider cells with active neighbours,
# so this function returns a cuboid one space bigger than the furthest active
# cell in each direction.
def get_bounds(active_cells):
    x_values = [cell[0] for cell in active_cells]
    y_values = [cell[1] for cell in active_cells]
    z_values = [cell[2] for cell in active_cells]

    return {
        'x_upper': max(x_values) + 1,
        'x_lower': min(x_values) - 1,
        'y_upper': max(y_values) + 1,
        'y_lower': min(y_values) - 1,
        'z_upper': max(z_values) + 1,
        'z_lower': min(z_values) - 1
    }


assert get_bounds([(0, 0, 0)]) == {
    'x_upper': 1,
    'x_lower': -1,
    'y_upper': 1,
    'y_lower': -1,
    'z_upper': 1,
    'z_lower': -1
}

assert get_bounds([(0, 0, 0), (12, -3, 5)]) == {
    'x_upper': 13,
    'x_lower': -1,
    'y_upper': 1,
    'y_lower': -4,
    'z_upper': 6,
    'z_lower': -1
}


def cycle(active_cells):
    bounds = get_bounds(active_cells)
    x_upper = bounds['x_upper']
    x_lower = bounds['x_lower']
    y_upper = bounds['y_upper']
    y_lower = bounds['y_lower']
    z_upper = bounds['z_upper']
    z_lower = bounds['z_lower']
    next_round = []

    for x in range(x_lower, x_upper + 1):
        for y in range(y_lower, y_upper + 1):
            for z in range(z_lower, z_upper + 1):
                n_neighbours = count_neighbours((x, y, z), active_cells)
                if (x, y, z) in active_cells and (n_neighbours == 2
                                                  or n_neighbours == 3):
                    next_round.append((x, y, z))
                if (x, y, z) not in active_cells and n_neighbours == 3:
                    next_round.append((x, y, z))

    return next_round


def human_friendly_print(active_cells):
    bounds = get_bounds(active_cells)
    # -1 because we don't need the buffer of empty cells for this purpose.
    x_lower = bounds['x_lower'] + 1
    x_upper = bounds['x_upper'] - 1
    y_lower = bounds['y_lower'] + 1
    y_upper = bounds['y_upper'] - 1
    z_lower = bounds['z_lower'] + 1
    z_upper = bounds['z_upper'] - 1

    for z in range(z_lower, z_upper + 1):
        print('z=' + str(z))
        for y in range(y_lower, y_upper + 1):
            row = ''
            for x in range(x_lower, x_upper + 1):
                if (x, y, z) in active_cells:
                    row += ACTIVE
                else:
                    row += INACTIVE
            print(row)
        print()


# round_one = cycle(sample_active_cells)
# human_friendly_print(round_one)

# round_two = cycle(round_one)
# human_friendly_print(round_two)

for i in range(0, 6):
    sample_active_cells = cycle(sample_active_cells)

for i in range(0, 6):
    active_cells = cycle(active_cells)

n_sample_after_six_cycles = len(sample_active_cells)
print(n_sample_after_six_cycles)
assert n_sample_after_six_cycles == 112

n_after_six_cycles = len(active_cells)
print(n_after_six_cycles)
assert n_after_six_cycles == 395