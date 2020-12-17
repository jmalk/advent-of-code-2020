with open('sample-input.txt') as f:
    sample_text = f.read()
f.close()

with open('input.txt') as f:
    text = f.read()
f.close()


def inclusive_range(string):
    # Won't handle negative numbers because splitting on hyphen
    str_bounds = string.split('-')
    int_bounds = [int(s) for s in str_bounds]
    return list(range(int_bounds[0], int_bounds[1] + 1))


assert inclusive_range('1-3') == [1, 2, 3]
assert inclusive_range('2-7') == [2, 3, 4, 5, 6, 7]


def get_ticket_rules(input_text):
    data_blocks = input_text.split('\n\n')
    ticket_rules = data_blocks[0].split('\n')
    ticket_rules = [rule.split(': ') for rule in ticket_rules]
    ticket_rules = [[rule[0], rule[1].split(' or ')] for rule in ticket_rules]
    ticket_rules_dict = {}
    for rule in ticket_rules:
        key_name = rule[0]
        ticket_rules_dict[key_name] = []
        list_bounds = rule[1]
        for bounds in list_bounds:
            ticket_rules_dict[key_name].extend(inclusive_range(bounds))
    return ticket_rules_dict


assert get_ticket_rules(sample_text) == {
    'class': [1, 2, 3, 5, 6, 7],
    'row':
    [6, 7, 8, 9, 10, 11, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],
    'seat': [
        13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50
    ]
}


def get_your_ticket_numbers(input_text):
    data_blocks = input_text.split('\n\n')
    your_ticket = data_blocks[1].split('\n')
    your_ticket_values = your_ticket[1].split(',')
    return [int(val) for val in your_ticket_values]


assert get_your_ticket_numbers(sample_text) == [7, 1, 14]


def get_nearby_tickets(input_text):
    data_blocks = input_text.split('\n\n')
    nearby_tickets = data_blocks[2].split('\n')
    # Ignore first as it is just string "nearby tickets"
    nearby_tickets = nearby_tickets[1:]
    nearby_tickets = [string.split(',') for string in nearby_tickets]
    nearby_ticket_numbers = []
    for ticket in nearby_tickets:
        ticket_numbers = [int(string) for string in ticket]
        nearby_ticket_numbers.append(ticket_numbers)
    return nearby_ticket_numbers


assert get_nearby_tickets(sample_text) == [[7, 3, 47], [40, 4, 50],
                                           [55, 2, 20], [38, 6, 12]]

sample_rules = get_ticket_rules(sample_text)
sample_nearby_tickets = get_nearby_tickets(sample_text)
rules = get_ticket_rules(text)
nearby_tickets = get_nearby_tickets(text)


def error_number(ticket, rules):
    error_number = 0
    all_valid_numbers = []
    for rule in rules:
        all_valid_numbers.extend(rules[rule])
    for number in ticket:
        if number not in all_valid_numbers:
            error_number += number
    return error_number


assert error_number(sample_nearby_tickets[0], sample_rules) == 0
assert error_number(sample_nearby_tickets[1], sample_rules) == 4
assert error_number(sample_nearby_tickets[2], sample_rules) == 55
assert error_number(sample_nearby_tickets[3], sample_rules) == 12


def error_total(tickets, rules):
    return sum([error_number(ticket, rules) for ticket in tickets])


assert error_total(sample_nearby_tickets, sample_rules) == 71

part_1 = error_total(nearby_tickets, rules)
print('Part 1:', part_1)
assert part_1 == 23054
