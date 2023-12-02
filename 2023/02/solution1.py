"""
Solution for day #2 Advent of Code 2013

https://adventofcode.com/2023/day/2
"""

import re

class Color(int):
    def __init__(self, value: int):
        if value < 0: raise ValueError("cannot be negative")
        if int(value) != value: raise ValueError("must be an integer")

class Bag():
    red: Color = 0
    green: Color = 0
    blue: Color = 0

    def __init__(self, s: str = None):
        if s is None:
            return
        for stone_count in s.split(','):
            number = int(re.sub(r'[^0-9]', '', stone_count))
            if 'red' in stone_count:
                self.red = number
            if 'green' in stone_count:
                self.green = number
            if 'blue' in stone_count:
                self.blue = number

    def is_possible(self, turn) -> bool:
        return turn.red <= self.red and \
                turn.green <= self.green and \
                turn.blue <= self.blue


bag = Bag("12 red, 13 green, 14 blue")

with open('input.txt') as f:
    data = f.read().strip()

good_ids = []
for line in data.split('\n'):
    game = line.strip().split(':')
    game_id = re.sub(r'[^-0-9]', '', game[0])
    assert re.match(r'^[0-9]+$', game_id), "game ID is not a natural number"
    game_id = int(game_id)
    turns = [Bag(s) for s in game[1].split(';')]
    repr(turns)
    if all([bag.is_possible(turn) for turn in turns]):
        good_ids.append(game_id)

print("games that can be played:", good_ids)
result = sum(good_ids)
print(result)
