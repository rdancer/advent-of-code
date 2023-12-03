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

list = []
for line in data.split('\n'):
    line = line.strip()

print("list:", list)
result = sum(list)
print(result)
