# First turns, total turns, expected result
test_cases = [([0, 3, 6], 2020, 436), ([1, 3, 2], 2020, 1),
              ([2, 1, 3], 2020, 10), ([1, 2, 3], 2020, 27),
              ([2, 3, 1], 2020, 78), ([3, 2, 1], 2020, 438),
              ([3, 1, 2], 2020, 1836)]


def find_last_index(list, target):
    for i in range(len(list) - 1, -1, -1):
        if list[i] == target:
            return i
    return None


assert find_last_index([1, 2, 3], 3) == 2
assert find_last_index([3, 2, 3], 3) == 2
assert find_last_index([3, 2, 3], 4) == None
assert find_last_index([], 3) == None


def turn(prev_turns):
    new_turns = prev_turns.copy()
    most_recent_turn = prev_turns[-1]
    history = prev_turns[0:-1]

    if most_recent_turn not in history:
        new_turns.append(0)
    else:
        previous_index = find_last_index(history, most_recent_turn)
        most_recent_index = len(prev_turns) - 1
        delta = most_recent_index - previous_index
        new_turns.append(delta)

    return new_turns


assert turn([0, 3, 6]) == [0, 3, 6, 0]
assert turn([0, 3, 6, 0]) == [0, 3, 6, 0, 3]
assert turn([0, 3, 6, 0, 3]) == [0, 3, 6, 0, 3, 3]
assert turn([0, 3, 6, 0, 3, 3]) == [0, 3, 6, 0, 3, 3, 1]
assert turn([0, 3, 6, 0, 3, 3, 1]) == [0, 3, 6, 0, 3, 3, 1, 0]
assert turn([0, 3, 6, 0, 3, 3, 1, 0]) == [0, 3, 6, 0, 3, 3, 1, 0, 4]
assert turn([0, 3, 6, 0, 3, 3, 1, 0, 4]) == [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]


def play_until(opening_turns, n_turns):
    turns = opening_turns.copy()
    while len(turns) < n_turns:
        if len(turns) % 1000 == 0:
            print(len(turns))
        turns = turn(turns)
    return turns[-1]


for case in test_cases:
    assert play_until(case[0], case[1]) == case[2]

part_1 = play_until([1, 0, 16, 5, 17, 4], 2020)
print('Part 1:', part_1)
assert part_1 == 1294

part_2 = play_until([1, 0, 16, 5, 17, 4], 30000000)
