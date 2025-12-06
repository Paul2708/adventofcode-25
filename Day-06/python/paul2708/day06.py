from typing import List, Optional, Tuple

from shared.paul2708.input_reader import *
from shared.paul2708.output import write
from shared.paul2708.utility import copy_list

grid = [[k for k in line.strip().split(" ") if k != ""] for line in read_plain_input(day=6, example=None)]

total = 0
for j in range(len(grid[0])):
    nums = []

    for i in range(len(grid)):

        if grid[i][j] == "+":
            total += sum(nums)
        elif grid[i][j] == "*":
            a = 1
            for b in nums:
                a *= b
            total += a
        else:
            nums.append(int(grid[i][j]))

print(total)