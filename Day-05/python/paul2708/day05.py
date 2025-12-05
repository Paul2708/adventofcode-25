from typing import List

import tqdm

from shared.paul2708.input_reader import *
from shared.paul2708.output import write

lines = read_plain_input(day=5, example=1)

fresh_id_ranges = []
ids = []

a = True
for line in lines:
    if line == "":
        a = False
        continue
    if a:
        x = line.split("-")
        fresh_id_ranges.append((int(x[0]), int(x[1])))
    else:
        ids.append(int(line))

print(fresh_id_ranges)
print(ids)

c = 0

for i in ids:
    for a, b in fresh_id_ranges:
        if a <= i <= b:
            c += 1
            break

print(c)

clean_id_ranges = []
clean_id_ranges.append(fresh_id_ranges[0])

def merge(a, b, x, y):
    for i in range(len(clean_id_ranges)):
        clean_a, clean_b = clean_id_ranges[i][0], clean_id_ranges[i][1]

        if clean_a <= a <= b <= clean_b:
            print("Included")
            break

        if clean_a <= a <= clean_b <= b:
            clean_id_ranges[i] = (clean_a, b)
            print("Right overlap")
            break

        if a <= clean_a <= b <= clean_b:
            clean_id_ranges[i] = (a, clean_b)
            print("Left overlap")
            break

        if a <= clean_a <= clean_b <= b:
            clean_id_ranges[i] = (a, b)
            print("Both overlap")
            break

        clean_id_ranges.append((a, b))
        print("New")


for a, b in fresh_id_ranges[1:]:
    print(a, b)
    for i in range(len(clean_id_ranges)):
        clean_a, clean_b = clean_id_ranges[i][0], clean_id_ranges[i][1]

        if clean_a <= a <= b <= clean_b:
            done = True
            print("Included")
            break

        if clean_a <= a <= clean_b <= b:
            clean_id_ranges[i] = (clean_a, b)
            print("Right overlap")
            break

        if a <= clean_a <= b <= clean_b:
            clean_id_ranges[i] = (a, clean_b)
            print("Left overlap")
            break

        if a <= clean_a <= clean_b <= b:
            clean_id_ranges[i] = (a, b)
            print("Both overlap")
            break

        clean_id_ranges.append((a, b))
        print("New")

total = 0

for a, b in clean_id_ranges:
    total += b - a + 1

print(total)
print(clean_id_ranges)
