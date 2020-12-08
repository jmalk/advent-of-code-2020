with open('sample-input.txt') as f:
    sample_lines = f.readlines()
f.close()

with open('input.txt') as f:
    lines = f.readlines()
f.close()


def to_instruction(line):
    parts = line.split(' ')
    return (parts[0], int(parts[1]))


assert to_instruction('nop +0') == ('nop', +0)
assert to_instruction('acc -2') == ('acc', -2)
assert to_instruction('jmp +5') == ('jmp', +5)

sample_instructions = [to_instruction(line) for line in sample_lines]
instructions = [to_instruction(line) for line in lines]


def process_instruction(instruction, program_state):
    instruction_type = instruction[0]
    increment = instruction[1]

    acc = program_state["acc"]
    pointer = program_state["pointer"]

    if instruction_type == 'acc':
        return {"acc": acc + increment, "pointer": pointer + 1}
    if instruction_type == 'jmp':
        return {"acc": acc, "pointer": pointer + increment}
    # Default to 'nop' case
    return {"acc": acc, "pointer": pointer + 1}


# nop should move on to next instruction (increment pointer) and do nothing else
assert process_instruction(('nop', +0), {
    "acc": 0,
    "pointer": 0
}) == {
    "acc": 0,
    "pointer": 1
}

assert process_instruction(('nop', +0), {
    "acc": 11,
    "pointer": 3
}) == {
    "acc": 11,
    "pointer": 4
}

# acc should add to accumulator value and move on to next instruction (increment pointer)
assert process_instruction(('acc', +7), {
    "acc": 0,
    "pointer": 0
}) == {
    "acc": 7,
    "pointer": 1
}

assert process_instruction(('acc', +7), {
    "acc": -3,
    "pointer": 12
}) == {
    "acc": 4,
    "pointer": 13
}

# jmp should move pointer by value without changing accumulator
assert process_instruction(('jmp', +2), {
    "acc": 0,
    "pointer": 6
}) == {
    "acc": 0,
    "pointer": 8
}


def accumulator_before_repeat(program):
    lines_run = []
    would_repeat = False
    state = {'acc': 0, 'pointer': 0}

    while would_repeat == False:
        if state['pointer'] not in lines_run:
            lines_run.append(state['pointer'])
            state = process_instruction(program[state['pointer']], state)
        else:
            would_repeat = True

    return state['acc']


assert accumulator_before_repeat(sample_instructions) == 5

part_1 = accumulator_before_repeat(instructions)
print('Part 1:', part_1)
assert part_1 == 1451