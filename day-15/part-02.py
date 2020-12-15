# First turns, total turns, expected result
test_cases = [([0, 3, 6], 2020, 436), ([1, 3, 2], 2020, 1),
              ([2, 1, 3], 2020, 10), ([1, 2, 3], 2020, 27),
              ([2, 3, 1], 2020, 78), ([3, 2, 1], 2020, 438),
              ([3, 1, 2], 2020, 1836)]
'''
game_state
n_turns: int
latest_turn: int
history: <given_number: int, last_appeared_at: int>
'''


def turn(game_state):
    latest_turn = game_state['latest_turn']
    history = game_state['history']
    n_turns = game_state['n_turns']

    if n_turns % 1000 == 0:
        print('Reached turn', n_turns)

    if latest_turn in history:
        game_state['latest_turn'] = n_turns - history[latest_turn]
        game_state['history'][latest_turn] = n_turns
    else:
        game_state['latest_turn'] = 0
        game_state['history'][latest_turn] = n_turns

    game_state['n_turns'] += 1

    return game_state


def generate_initial_state(starting_turns):
    n_starting_turns = len(starting_turns)

    game_state = {
        'n_turns': n_starting_turns,
        'latest_turn': starting_turns[-1],
        'history': {}  # { Number: Turn it was last seen on }
    }

    for i in range(n_starting_turns - 1):
        game_state['history'][starting_turns[i]] = i + 1

    return game_state


assert generate_initial_state([0, 3, 6]) == {
    'n_turns': 3,
    'latest_turn': 6,
    'history': {
        0: 1,
        3: 2,
    }
}

after_fourth_turn = {
    'n_turns': 4,
    'latest_turn': 0,
    'history': {
        0: 1,
        3: 2,
        6: 3
    }
}
assert turn(generate_initial_state([0, 3, 6])) == after_fourth_turn

after_fifth_turn = {
    'n_turns': 5,
    'latest_turn': 3,
    'history': {
        3: 2,
        6: 3,
        0: 4
    }
}
assert turn(after_fourth_turn) == after_fifth_turn


def play_until(opening_turns, n_turns):
    game_state = generate_initial_state(opening_turns)
    while game_state['n_turns'] < n_turns:
        game_state = turn(game_state)
    return game_state['latest_turn']


play_until([0, 3, 6], 10)
for case in test_cases:
    assert play_until(case[0], case[1]) == case[2]

part_1 = play_until([1, 0, 16, 5, 17, 4], 2020)
print('Part 1:', part_1)
assert part_1 == 1294

part_2 = play_until([1, 0, 16, 5, 17, 4], 30000000)
print('Part 2:', part_2)
assert part_2 == 573522
