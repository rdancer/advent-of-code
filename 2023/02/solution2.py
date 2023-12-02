"""
Solution for day #2 Advent of Code 2013

https://adventofcode.com/2023/day/2
"""

import re
from functools import reduce
from operator import mul
from numbers import Number
from typing import Iterable

class Count(int):
    def __new__(cls, value: int) -> 'Count':
        if not isinstance(value, int): raise TypeError("must be an integer")
        if value < 0: raise ValueError("cannot be negative")
        return int.__new__(cls, value)

def product(iterable: Iterable[Number]) -> Number:
    return reduce(mul, iterable, 1)

def count_property(name):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name, 0)

    @prop.setter
    def prop(self, value):
        setattr(self, storage_name, Count(value))

    return prop

class Bag():
    red = count_property('red')
    green = count_property('green')
    blue = count_property('blue')

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

    def __iter__(self):
        yield self.red
        yield self.green
        yield self.blue

    def __repr__(self):
        return str({
            "red": self.red,
            "green": self.green,
            "blue": self. blue
        }) + f", power: {self.product()}"

    def minimum_enclosure(self, other):
        return Bag(f"{max(self.red, other.red)} red, {max(self.green, other.green)} green, {max(self.blue, other.blue)} blue")

    def is_possible(self, turn) -> bool:
        return turn.red <= self.red and \
                turn.green <= self.green and \
                turn.blue <= self.blue

    def product(self) -> int:
        return product(self)

    @classmethod
    def test(cls):
        assert repr(Bag('12 red, 13 green, 14 blue')) == "{'red': 12, 'green': 13, 'blue': 14}, power: 2184"
        try:
            Bag().red = 'foobar'
            raise Exception("type not enforced")
        except TypeError:
            pass
        try:
            Bag().green = -1
            raise Exception("negative assignment not prevented")
        except ValueError:
            pass
        return True

assert Bag.test(), "self-test failed"
    
with open('input.txt') as f:
    data = f.read().strip()

powers = []
for line in data.split('\n'):
    game = line.strip().split(':')
    game_id = re.sub(r'[^-0-9]', '', game[0])
    assert re.match(r'^[0-9]+$', game_id), "game ID is not a natural number"
    game_id = int(game_id)
    turns = [Bag(s) for s in game[1].split(';')]
    smallest_possible_bag = reduce(lambda a, b: a.minimum_enclosure(b), turns, Bag())
    print(repr(smallest_possible_bag))
    powers.append(smallest_possible_bag.product())

print("powers:", powers)
result = sum(powers)
print(result)
