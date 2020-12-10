with open('sample-input.txt') as f:
    sample_lines = f.readlines()
f.close

with open('input.txt') as f:
    lines = f.readlines()
f.close


def get_all_joltages(lines):
    numbers = [int(n) for n in lines]
    port_joltage = 0
    device_joltage = max(numbers) + 3
    numbers.extend([port_joltage, device_joltage])
    numbers.sort()
    return numbers


sample_numbers = get_all_joltages(sample_lines)
numbers = get_all_joltages(lines)


def get_joltage_diffs(joltages):
    joltage_diffs = {"1": 0, "3": 0}

    for i in range(0, len(joltages) - 1):
        diff = joltages[i + 1] - joltages[i]
        if diff == 1:
            joltage_diffs['1'] += 1
        if diff == 3:
            joltage_diffs['3'] += 1

    return joltage_diffs


sample_joltage_diffs = get_joltage_diffs(sample_numbers)
joltage_diffs = get_joltage_diffs(numbers)

assert sample_joltage_diffs['1'] == 22
assert sample_joltage_diffs['3'] == 10


def get_product(joltage_diffs):
    return joltage_diffs['1'] * joltage_diffs['3']


sample_product = get_product(sample_joltage_diffs)
assert sample_product == 220

part_1 = get_product(joltage_diffs)
print('Part 1:', part_1)
