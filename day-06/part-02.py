with open('input.txt', 'r') as f:
    file_string = ''.join(f.readlines())
f.close()


def count_shared_characters(strings):
    # For a list of strings, return the number of characters that appear in all of the strings
    count = 0
    for char in strings[0]:
        if all([char in string for string in strings]):
            count += 1
    return count


assert count_shared_characters(['abc']) == 3
assert count_shared_characters(['a', 'b', 'c']) == 0
assert count_shared_characters(['ab', 'ac']) == 1
assert count_shared_characters(['a', 'a', 'a', 'a']) == 1
assert count_shared_characters(['b']) == 1

groups = [string.split('\n') for string in file_string.split('\n\n')]
sum_shared = sum([count_shared_characters(group) for group in groups])
assert sum_shared == 3260
print('Part 2: ', sum_shared)