sample_dict_bag_defintions = {
    'light red': ['1 bright white', '2 muted yellow'],
    'dark orange': ['3 bright white', '4 muted yellow'],
    'bright white': ['1 shiny gold'],
    'muted yellow': ['2 shiny gold', '9 faded blue'],
    'shiny gold': ['1 dark olive', '2 vibrant plum'],
    'dark olive': ['3 faded blue', '4 dotted black'],
    'vibrant plum': ['5 faded blue', '6 dotted black'],
    'faded blue': None,
    'dotted black': None
}

with open('input.txt', 'r') as f:
    lines = f.readlines()
f.close()

bag_definitions = [
    line.replace('\n', '').split(' bags contain ') for line in lines
]

for defn in bag_definitions:
    defn[1] = defn[1].replace(' bags', '').replace(' bag', '').replace('.', '')
    defn[1] = defn[1].split(', ')
    if defn[1] == ['no other']:
        defn[1] = None

dict_bag_definitions = dict(bag_definitions)


def find_immediate_containers_of(color, bags):
    containers = []
    for bag in bags:
        if bags[bag] != None:  # TODO: make separate filter for this, reduce nesting.
            for string in bags[bag]:
                if color in string:
                    containers.append(bag)
    return list(set(containers))


immediate_containers = find_immediate_containers_of(
    'shiny gold', sample_dict_bag_defintions)
assert 'bright white' in immediate_containers
assert 'muted yellow' in immediate_containers
assert len(immediate_containers) == 2


def find_containers_of(color, bags):
    new_containers = find_immediate_containers_of(color, bags)
    all_containers = []
    all_containers.extend(new_containers)

    while len(new_containers) > 0:
        # children = new_containers.copy()
        # new_containers = []
        found = []
        for color in new_containers:
            found.extend(find_immediate_containers_of(color, bags))
        deduped = list(set(found))
        all_containers.extend(deduped)
        new_containers = deduped
    return list(set(all_containers))


containers = find_containers_of('shiny gold', sample_dict_bag_defintions)
assert 'bright white' in containers
assert 'muted yellow' in containers
assert 'dark orange' in containers
assert 'light red' in containers
assert len(containers) == 4

print(find_containers_of('shiny gold', dict_bag_definitions))
shiny_gold_containers = find_containers_of('shiny gold', dict_bag_definitions)
num_shiny_gold_containers = len(shiny_gold_containers)
print('Part 1: ', num_shiny_gold_containers)  # 492, too high
