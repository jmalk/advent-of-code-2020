from functools import reduce

with open('sample-input.txt') as f:
    sample_lines = f.read().splitlines()
f.close()

with open('input.txt') as f:
    lines = f.read().splitlines()
f.close()

sample_ready_time = int(sample_lines[0])
ready_time = int(lines[0])

sample_bus_string = sample_lines[1]
bus_string = lines[1]

sample_bus_string_array = sample_bus_string.split(',')
bus_string_array = bus_string.split(',')

not_x = lambda string: string != 'x'

assert not_x('x') == False
assert not_x('y') == True

sample_bus_ids = [
    int(string) for string in filter(not_x, sample_bus_string_array)
]

bus_ids = [int(string) for string in filter(not_x, bus_string_array)]

sample_bus_times = [{
    'bus_id': bus_id,
    'wait': bus_id - (sample_ready_time % bus_id)
} for bus_id in sample_bus_ids]

bus_times = [{
    'bus_id': bus_id,
    'wait': bus_id - (ready_time % bus_id)
} for bus_id in bus_ids]

smaller_wait = lambda a, b: a if a['wait'] < b['wait'] else b

sample_soonest_bus = reduce(smaller_wait, sample_bus_times)
sample_answer = sample_soonest_bus['bus_id'] * sample_soonest_bus['wait']
assert sample_answer == 295

soonest_bus = reduce(smaller_wait, bus_times)
part_1 = soonest_bus['bus_id'] * soonest_bus['wait']
print('Part 1:', part_1)
assert part_1 == 3269