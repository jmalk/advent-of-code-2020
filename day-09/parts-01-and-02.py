with open('sample-input.txt') as f:
    sample_lines = f.readlines()
f.close()

with open('input.txt') as f:
    lines = f.readlines()
f.close()

sample_numbers = [int(l) for l in sample_lines]
numbers = [int(l) for l in lines]


def contains_pair_that_sum_to(numbers, target):
    for i in range(0, len(numbers)):
        a = numbers[i]
        for j in range(i + 1, len(numbers)):
            b = numbers[j]
            if a + b == target:
                return True
    return False


assert contains_pair_that_sum_to([1, 2], 3) == True
assert contains_pair_that_sum_to([1, 2, 3], 6) == False  # Can't use 3 twice


def first_invalid_number(numbers, preamble=25):
    for i in range(preamble, len(numbers)):
        current_number = numbers[i]
        preceding = numbers[i - preamble:i]
        valid = contains_pair_that_sum_to(preceding, current_number)
        if not valid:
            return current_number
    return None


assert first_invalid_number(sample_numbers, preamble=5) == 127

part_1 = first_invalid_number(numbers)
print('Part 1:', part_1)
assert part_1 == 32321523


def find_contiguous_sublist_that_sum_to(numbers, target):
    for i in range(0, len(numbers)):
        for j in range(1, len(numbers) - i):
            total = sum(numbers[i:i + j])
            # Stop if it's already bigger than the target
            # Adding more numbers won't help
            # This assumes all numbers are positive though!
            if total > target:
                break
            if total == target:
                return numbers[i:i + j]
    return None


assert find_contiguous_sublist_that_sum_to(sample_numbers,
                                           127) == [15, 25, 47, 40]


def sum_min_max(numbers):
    smallest = min(numbers)
    biggest = max(numbers)
    return smallest + biggest


assert sum_min_max([1, 2, 3]) == 4
assert sum_min_max([2, 1, 3]) == 4

part_2 = sum_min_max(find_contiguous_sublist_that_sum_to(numbers, part_1))
print('Part 2', part_2)
assert part_2 == 4794981
