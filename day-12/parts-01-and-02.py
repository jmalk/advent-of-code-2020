with open('sample-input.txt') as f:
    sample_lines = f.read().splitlines()
f.close()

with open('input.txt') as f:
    lines = f.read().splitlines()
f.close


def to_instruction(string):
    return {'kind': string[0], 'amount': int(string[1:])}


assert to_instruction('F10') == {'kind': 'F', 'amount': 10}

sample_instructions = [to_instruction(string) for string in sample_lines]
instructions = [to_instruction(string) for string in lines]

# State
# position_north: int, position_east: int, heading: 'N' | 'E' | 'S' | 'W'

initial_state = {'position_north': 0, 'position_east': 0, 'heading': 'E'}


def turn_right(initial_heading, degrees):
    headings = ['N', 'E', 'S', 'W']
    quarter_turns = int(degrees / 90)
    start_index = headings.index(initial_heading)
    new_index = (start_index + quarter_turns) % 4
    new_heading = headings[new_index]
    return new_heading


def turn_left(initial_heading, degrees):
    headings = ['N', 'W', 'S', 'E']
    quarter_turns = int(degrees / 90)
    start_index = headings.index(initial_heading)
    new_index = (start_index + quarter_turns) % 4
    new_heading = headings[new_index]
    return new_heading


# Turn right tests

assert turn_right('N', 0) == 'N'
assert turn_right('N', 90) == 'E'
assert turn_right('N', 180) == 'S'
assert turn_right('N', 270) == 'W'

assert turn_right('E', 0) == 'E'
assert turn_right('E', 90) == 'S'
assert turn_right('E', 180) == 'W'
assert turn_right('E', 270) == 'N'

assert turn_right('S', 0) == 'S'
assert turn_right('S', 90) == 'W'
assert turn_right('S', 180) == 'N'
assert turn_right('S', 270) == 'E'

assert turn_right('W', 0) == 'W'
assert turn_right('W', 90) == 'N'
assert turn_right('W', 180) == 'E'
assert turn_right('W', 270) == 'S'

#Turn left tests

assert turn_left('N', 0) == 'N'
assert turn_left('N', 90) == 'W'
assert turn_left('N', 180) == 'S'
assert turn_left('N', 270) == 'E'

assert turn_left('E', 0) == 'E'
assert turn_left('E', 90) == 'N'
assert turn_left('E', 180) == 'W'
assert turn_left('E', 270) == 'S'

assert turn_left('S', 0) == 'S'
assert turn_left('S', 90) == 'E'
assert turn_left('S', 180) == 'N'
assert turn_left('S', 270) == 'W'

assert turn_left('W', 0) == 'W'
assert turn_left('W', 90) == 'S'
assert turn_left('W', 180) == 'E'
assert turn_left('W', 270) == 'N'


def move(instruction, state):
    new_state = {
        'position_north': state['position_north'],
        'position_east': state['position_east'],
        'heading': state['heading']
    }
    if instruction['kind'] == 'F':
        h = state['heading']
        if h == 'N':
            new_state['position_north'] += instruction['amount']
        if h == 'S':
            new_state['position_north'] -= instruction['amount']
        if h == 'E':
            new_state['position_east'] += instruction['amount']
        if h == 'W':
            new_state['position_east'] -= instruction['amount']

    elif instruction['kind'] == 'N':
        new_state['position_north'] += instruction['amount']

    elif instruction['kind'] == 'S':
        new_state['position_north'] -= instruction['amount']

    elif instruction['kind'] == 'E':
        new_state['position_east'] += instruction['amount']

    elif instruction['kind'] == 'W':
        new_state['position_east'] -= instruction['amount']

    elif instruction['kind'] == 'R':
        new_state['heading'] = turn_right(state['heading'],
                                          instruction['amount'])

    elif instruction['kind'] == 'L':
        new_state['heading'] = turn_left(state['heading'],
                                         instruction['amount'])

    return new_state


first_sample_state = move(to_instruction('F10'), initial_state)
assert first_sample_state == {
    'position_north': 0,
    'position_east': 10,
    'heading': 'E'
}

second_sample_state = move(to_instruction('N3'), first_sample_state)
assert second_sample_state == {
    'position_north': 3,
    'position_east': 10,
    'heading': 'E'
}

third_sample_state = move(to_instruction('F7'), second_sample_state)
assert third_sample_state == {
    'position_north': 3,
    'position_east': 17,
    'heading': 'E'
}

fourth_sample_state = move(to_instruction('R90'), third_sample_state)
assert fourth_sample_state == {
    'position_north': 3,
    'position_east': 17,
    'heading': 'S'
}

fifth_sample_state = move(to_instruction('F11'), fourth_sample_state)
assert fifth_sample_state == {
    'position_north': -8,
    'position_east': 17,
    'heading': 'S'
}


def final_manhattan_distance(instructions, initial_state):
    state = initial_state
    for instruction in instructions:
        state = move(instruction, state)
    final_north = state['position_north']
    final_east = state['position_east']
    manhattan_distance = abs(final_north) + abs(final_east)
    return manhattan_distance


assert final_manhattan_distance(sample_instructions, initial_state) == 25

part_1 = final_manhattan_distance(instructions, initial_state)
print('Part 1:', part_1)
assert part_1 == 590
