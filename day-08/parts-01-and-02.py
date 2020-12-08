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
        return {"acc": acc + increment, "pointer": pointer + 1, "error": None}
    if instruction_type == 'jmp':
        return {"acc": acc, "pointer": pointer + increment, "error": None}
    # Default to 'nop' case
    return {"acc": acc, "pointer": pointer + 1, "error": None}


# nop should move on to next instruction (increment pointer) and do nothing else
assert process_instruction(('nop', +0), {
    "acc": 0,
    "pointer": 0,
    "error": None
}) == {
    "acc": 0,
    "pointer": 1,
    "error": None
}

assert process_instruction(('nop', +0), {
    "acc": 11,
    "pointer": 3,
    "error": None
}) == {
    "acc": 11,
    "pointer": 4,
    "error": None
}

# acc should add to accumulator value and move on to next instruction (increment pointer)
assert process_instruction(('acc', +7), {
    "acc": 0,
    "pointer": 0,
    "error": None
}) == {
    "acc": 7,
    "pointer": 1,
    "error": None
}

assert process_instruction(('acc', +7), {
    "acc": -3,
    "pointer": 12,
    "error": None
}) == {
    "acc": 4,
    "pointer": 13,
    "error": None
}

# jmp should move pointer by value without changing accumulator
assert process_instruction(('jmp', +2), {
    "acc": 0,
    "pointer": 6,
    "error": None
}) == {
    "acc": 0,
    "pointer": 8,
    "error": None
}

error_codes = {'INFINITE': 'infinite loop'}


def run_program(program):
    lines_run = []
    ended = False
    state = {'acc': 0, 'pointer': 0, 'error': None}

    while ended == False:
        # If program reaches the index immediately after instructions,
        # it terminates
        if state['pointer'] == len(program):
            ended = True
        elif state['pointer'] not in lines_run:
            lines_run.append(state['pointer'])
            state = process_instruction(program[state['pointer']], state)
        else:
            ended = True
            state['error'] = error_codes['INFINITE']

    return state


assert run_program(sample_instructions)['acc'] == 5
assert run_program(sample_instructions)['error'] == error_codes['INFINITE']

part_1 = run_program(instructions)['acc']
print('Part 1:', part_1)
assert part_1 == 1451


def try_fixing_program(program):
    swaps = {'jmp': 'nop', 'nop': 'jmp'}

    for i in range(len(program)):
        instruction = program[i]
        instruction_type = instruction[0]
        if instruction_type in swaps:
            program_copy = program.copy()
            program_copy[i] = (swaps[instruction_type], program_copy[i][1])
            result = run_program(program_copy)
            if result['error'] == None:
                return result['acc']


assert try_fixing_program(sample_instructions) == 8
part_2 = try_fixing_program(instructions)
print('Part 2:', part_2)
