# First turns, total turns, expected result
test_cases = [([0, 3, 6], 2020, 436), ([1, 3, 2], 2020, 1),
              ([2, 1, 3], 2020, 10), ([1, 2, 3], 2020, 27),
              ([2, 3, 1], 2020, 78), ([3, 2, 1], 2020, 438),
              ([3, 1, 2], 2020, 1836)]
'''
game_state
n_turns: int
latest_turn: int
history: <given_number: int, n_turns: int>
'''


def turn(game_state):
    latest_turn = game_state['latest_turn']
    history = game_state['history']
    n_turns = game_state['n_turns']

    if n_turns % 1000 == 0:
        print(n_turns)

    if latest_turn in history:
        game_state['latest_turn'] = history[latest_turn]
        for key in game_state['history']:
            game_state['history'][key] += 1
        game_state['history'][latest_turn] = 1
    else:
        game_state['latest_turn'] = 0
        for key in game_state['history']:
            game_state['history'][key] += 1
        game_state['history'][latest_turn] = 1

    game_state['n_turns'] += 1

    return game_state


def generate_initial_state(starting_turns):
    n_starting_turns = len(starting_turns)

    game_state = {
        'n_turns': n_starting_turns,
        'latest_turn': starting_turns[-1],
        'history': {}
    }

    for i in range(n_starting_turns - 1):
        game_state['history'][starting_turns[i]] = (n_starting_turns - 1) - i

    return game_state


assert generate_initial_state([0, 3, 6]) == {
    'n_turns': 3,
    'latest_turn': 6,
    'history': {
        0: 2,
        3: 1,
    }
}


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
