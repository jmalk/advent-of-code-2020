with open('input.txt', 'r') as f:
    file_string = ''.join(f.readlines())
f.close()

group_answers = [s.replace('\n', '') for s in file_string.split('\n\n')]
sum_uniques = sum([len(set(answers)) for answers in group_answers])
assert sum_uniques == 6457
print('Part 1: ', sum_uniques)