"""
Solution for day #3 Advent of Code 2013

https://adventofcode.com/2023/day/3
"""

import re
from functools import reduce
from operator import mul
from numbers import Number
from typing import List

with open('input.txt') as f:
    data = f.read().strip()

def pad_data(data):
    """Pad whole perimeter"""
    lines = data.split('\n')
    lines = [f".{line}." for line in lines]
    padding = ''.join(['.' for _ in lines[0]])
    lines = [padding] + lines + [padding]
    return '\n'.join(lines)

def adjacent_gears(lines: List[str], i: int, end_ptr: int, number: int) -> List[str]:
    """
    @return list of gear co-ordinates
    """
    length = len(str(number))
    first = end_ptr - length
    last = end_ptr + 1
    context = lines[i-1:i+2]
    context = [line[first:last+1] for line in context]
    context[1] = context[1][0] + ("." * length) +  context[1][-1]
    if re.search(r'\*', ''.join(context)):
        gear_coordinates = []
        for index, line in enumerate(context):
            gear_coordinates += [[index, match.start()] for match in re.finditer(r'\*', line)]
        gear_coordinates = [[coord[0] + i-1, coord[1] + first] for coord in gear_coordinates]
        gear_coordinates = [f"{coord[0]}x{coord[1]}" for coord in gear_coordinates]
        return gear_coordinates
    return []

gear_candidates = {}
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
            gears = adjacent_gears(lines, i, cursor-1, number)
            for gear in gears:
                if gear not in gear_candidates:
                    gear_candidates[gear] = []
                gear_candidates[gear].append(number)
            number = None

gear_ratios = []
for coord in gear_candidates:
    print("gear:", gear_candidates[coord])
    x = gear_candidates[coord]
    if len(x) == 2:
        gear_ratios.append(x[0] * x[1])
    
print("gear_ratios:", gear_ratios)
result = sum(gear_ratios)
print(result)
