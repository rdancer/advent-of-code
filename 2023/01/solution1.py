#!/usr/bin/env python3

import re

with open("input.txt") as f:
    data = f.read().strip()

numbers = []
for line in data.split('\n'):
    line = line.strip()
    line = re.sub(r'[^0-9]', '', line)
    if len(line) == 0:
        continue
    s = f"{line[0]}{line[-1]}" # Note that if the line only has one number, it is used twice
    numbers.append(int(s))

print(numbers)
print(sum(numbers))
