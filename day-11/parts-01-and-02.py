with open('sample-input.txt') as f:
    sample_lines = f.read().splitlines()
f.close()

sample_map = [list(line) for line in sample_lines]

with open('input.txt') as f:
    lines = f.read().splitlines()
f.close()

seating_map = [list(line) for line in lines]

expect_after_round_1 = '''#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
'''

expect_after_round_2 = '''#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
'''

expect_after_round_3 = '''#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
'''


def neighbours(seat, seating):
    seat_x = seat['column']
    seat_y = seat['row']

    left_bound = max([seat_x - 1, 0])
    right_bound = min([seat_x + 1, len(seating[seat_y]) - 1])
    top_bound = max([seat_y - 1, 0])
    bottom_bound = min([seat_y + 1, len(seating) - 1])

    total = 0
    for x in range(left_bound, right_bound + 1):
        for y in range(top_bound, bottom_bound + 1):
            # print('x', x, 'y', y)
            if seating[y][x] == '#' and not (x == seat_x and y == seat_y):
                total += 1
    return total


assert neighbours({
    'row': 1,
    'column': 1
}, [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]) == 8

assert neighbours({
    'row': 0,
    'column': 0
}, [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]) == 3

assert neighbours({
    'row': 2,
    'column': 0
}, [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]) == 3

assert neighbours({
    'row': 2,
    'column': 2
}, [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]) == 3

assert neighbours({
    'row': 0,
    'column': 2
}, [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]) == 3

assert neighbours({
    'row': 1,
    'column': 1
}, [['#', '#', '#'], ['.', '.', '.'], ['.', '#', '#']]) == 5


def overcrowded(seat, seating):
    return neighbours(seat, seating) >= 4


def no_neighbours(seat, seating):
    return neighbours(seat, seating) == 0


def next_round(seating):
    result = []
    changed = False
    for y in range(0, len(seating)):
        new_row = []
        for x in range(0, len(seating[y])):
            seat = {'row': y, 'column': x}
            current = seating[y][x]
            if current == '.':
                new_row.append('.')
            if current == '#':
                if overcrowded(seat, seating):
                    new_row.append('L')
                    changed = True
                else:
                    new_row.append('#')
            if current == 'L':
                if no_neighbours(seat, seating):
                    new_row.append('#')
                    changed = True
                else:
                    new_row.append('L')
        result.append(new_row)
    return {'seating': result, 'stable': not changed}


def to_string(seating):
    result = ''
    for row in seating:
        result += ''.join(row) + '\n'
    return result


after_round_1 = next_round(sample_map)['seating']
actual_after_round_1 = to_string(after_round_1)
assert actual_after_round_1 == expect_after_round_1

after_round_2 = next_round(after_round_1)['seating']
actual_after_round_2 = to_string(after_round_2)
assert actual_after_round_2 == expect_after_round_2

after_round_3 = next_round(after_round_2)['seating']
actual_after_round_3 = to_string(after_round_3)
assert actual_after_round_3 == expect_after_round_3


def count_after_stable(initial_seating):
    latest_result = {'seating': initial_seating, 'stable': False}
    while not latest_result['stable']:
        latest_result = next_round(latest_result['seating'])

    stable_seating = latest_result['seating']
    num_occupied = 0
    for row in stable_seating:
        for place in row:
            if place == '#':
                num_occupied += 1
    return num_occupied


assert count_after_stable(sample_map) == 37

part_1 = count_after_stable(seating_map)
print('Part 1:', part_1)
assert part_1 == 2281
