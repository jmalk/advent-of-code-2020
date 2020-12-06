with open('input.txt', 'r') as f:
    file_string = ''.join(f.readlines())
f.close()

group_strings = [s.replace('\n', '') for s in file_string.split('\n\n')]
sum_uniques = sum([len(set(g)) for g in group_strings])
assert sum_uniques == 6457
print('Part 1: ', sum_uniques)