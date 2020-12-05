with open('input.txt', 'r') as f:
    lines = f.readlines()
f.close()

tickets = [l.replace("\n", "") for l in lines]


def convert_to_binary(string_FBLR):
    binary_result = ''
    mapping = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
    for char in string_FBLR:
        binary_result += mapping[char]
    return binary_result


assert (convert_to_binary('FBLR') == '0101')


def get_column(seat_code):
    return seat_code[-3:]


assert get_column('FBFBBFFRLR') == 'RLR'


def get_row(seat_code):
    return seat_code[:7]


assert get_row('FBFBBFFRLR') == 'FBFBBFF'


def get_ticket_id(seat_code):
    as_binary = convert_to_binary(seat_code)
    row = int(get_row(as_binary), 2)
    column = int(get_column(as_binary), 2)
    return row * 8 + column


sample_string = 'FBFBBFFRLR'
assert get_ticket_id(sample_string) == 357

all_ids = [get_ticket_id(ticket) for ticket in tickets]
largest_id = max(all_ids)
assert largest_id == 855

print('Part 1: ', largest_id)

my_seat = -1
for seat_id in range(0, largest_id):
    empty_seat = seat_id not in all_ids
    real_seat = (seat_id + 1) in all_ids and (seat_id - 1) in all_ids
    if empty_seat and real_seat:
        my_seat = seat_id

assert my_seat == 552
print('Part 2: ', my_seat)