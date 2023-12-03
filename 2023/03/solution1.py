"""
Solution for day #3 Advent of Code 2013

https://adventofcode.com/2023/day/3
"""

import re
from functools import reduce
from operator import mul
from numbers import Number

with open('input.txt') as f:
    data = f.read().strip()

def pad_data(data):
    """Pad whole perimeter"""
    lines = data.split('\n')
    lines = [f".{line}." for line in lines]
    padding = ''.join(['.' for _ in lines[0]])
    lines = [padding] + lines + [padding]
    return '\n'.join(lines)

def is_adjacent_to_symbol(context, end_ptr: int, number: int):
    length = len(str(number))
    first = end_ptr - length
    last = end_ptr + 1
    context = [line[first:last+1] for line in context]
    context[1] = context[1][0] + context[1][-1]
    context = ''.join(context)
    if re.search(r'[^0-9\.]', context):
        return True
    return False

adjacents = []
data = pad_data(data)
lines = [line.strip() for line in data.split('\n')]
for i in range(1, len(lines)):
    cursor = 0
    number = None
    for cursor, c in enumerate(lines[i]):
        if c.isdigit():
            if number is None:
                number = 0
            number *= 10
            number += int(c)
        elif number is not None: # Note that this will always hit, because of padding
            if is_adjacent_to_symbol(lines[i-1:i+2], cursor-1, number):
                adjacents.append(number)
            number = None

print("adjacents:", adjacents)
result = sum(adjacents)
print(result)
