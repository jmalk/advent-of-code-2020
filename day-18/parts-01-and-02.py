# types
# expression = number operator (number | expression)
# number
# operator


def tokenize(token):
    # TODO: Handle brackets. Eep!
    if token == '+':
        return {"kind": "plus"}

    if token == '*':
        return {"kind": "times"}

    return {"kind": "number", "value": int(token)}


def parse(expression):
    tokens = expression.split(' ')
    tokens = [tokenize(token) for token in tokens]
    return tokens


def evaluate(left, operator, right):
    if operator['kind'] == 'plus':
        return left['value'] + right['value']
    elif operator['kind'] == 'times':
        return left['value'] * right['value']


print(evaluate(*parse("5 + 3")))