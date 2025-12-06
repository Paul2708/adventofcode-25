import itertools
from typing import List, Optional, Tuple

from shared.paul2708.input_reader import *
from shared.paul2708.output import write
from shared.paul2708.utility import copy_list, transpose

trimmed_grid = [[k for k in line.strip().split(" ") if k != ""] for line in read_plain_input(day=6, example=None)]

print("Trimmed")
print(trimmed_grid)

grid = [line for line in read_plain_input(day=6, example=None)]
print("Grid")
grid.remove(grid[-1])
print(grid)


def split_numbers(line: str, max_lengths):
    splitted = []
    curr = ""

    for i in range(len(line)):
        if len(curr) < max_lengths[len(splitted)]:
            curr += line[i]
        else:
            splitted.append(curr)
            curr = ""

    while len(curr) < max_lengths[-1]:
        curr += " "

    splitted.append(curr)

    return splitted


def get_longest_word(i):
    return max(list(map(len, transpose(trimmed_grid)[i])))


fixed_grid = []
for i in range(len(grid)):
    fixed_grid.append(split_numbers(grid[i], [get_longest_word(j) for j in range(len(transpose(trimmed_grid)))]))

print(fixed_grid)
print(list(map(list, zip(*fixed_grid))))


def transform_numbers(nums):
    max_length = max([len(num) for num in nums])

    res = []
    for i in range(max_length):

        digits = ""

        for num in nums:
            if 0 <= i < len(num):
                digits += num[-i - 1]

        res.append(int(digits))

    return res


print("==")
t = 0

for i, col in enumerate(transpose(fixed_grid)):
    print(col)
    print(transform_numbers(col))
    print(trimmed_grid[-1][i])

    if trimmed_grid[-1][i] == "+":
        t += sum(transform_numbers(col))
    else:
        a = 1
        for k in transform_numbers(col):
            a *= k
        t += a

print(t)
