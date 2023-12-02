#!/usr/bin/env python3

import re

with open("input.txt") as f:
    data = f.read().strip()


def fix(s):
    spelled_out = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # Now we can have lines like 'eightwothree', which is interpreted as 823
    # (note the overlap 'eightwo' still counts as two digits!).  A simple
    # regexp won't work, we must be much more clever.
    buffer = ''
    for letter in s:
        buffer += letter
        for i, spelling in enumerate(spelled_out):
            # This is a bit hacky way to handle overlaps, but for our
            # particular replacement table it works well.
            replacement = f"{spelling[0]}{i+1}{spelling[-1]}"
            buffer = re.sub(rf'{spelling}', replacement, buffer)
    return buffer

numbers = []
for line in data.split('\n'):
    line = line.strip()
    line = fix(line)
    line = re.sub(r'[^0-9]', '', line)
    if len(line) == 0:
        continue
    s = f"{line[0]}{line[-1]}" # Note that if the line only has one number, it is used twice
    numbers.append(int(s))

print(numbers)
print(sum(numbers))
