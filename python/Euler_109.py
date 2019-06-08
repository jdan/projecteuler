# Euler 109 solution
# 8 Jun 2019

import itertools

zero = (0, 0)
singles = map(lambda i: (1, i), range(1, 21) + [25])
doubles = map(lambda i: (2, i), range(1, 21) + [25])
triples = map(lambda i: (3, i), range(1, 21))

possible_closes = itertools.product(
    [zero] + singles + doubles + triples,
    [zero] + singles + doubles + triples,
    doubles
)

def make_setoid(first, second, third):
    return (frozenset([first, second]), third)

def print_throw(throw):
    multiplier, value = throw
    return {
        0: '',
        1: 'S',
        2: 'D',
        3: 'T',
    }[multiplier] + str(value)

def print_close(close):
    return " ".join([print_throw(throw) for throw in close])

def score_throw(throw):
    multiplier, value = throw
    return multiplier * value

def score_close(close):
    return sum([score_throw(throw) for throw in close])

def array_of_setoid(setoid):
    pair, third = setoid
    if len(pair) == 1:
        first = list(pair)[0]
        second = list(pair)[0]
    else:
        first, second = pair

    return [first, second, third]

deduped_closes = map(array_of_setoid, set(
    make_setoid(*close)
    for close in possible_closes
))

# print len(deduped_closes)
# => 42336

print len(filter(lambda c: score_close(c) < 100, deduped_closes))
