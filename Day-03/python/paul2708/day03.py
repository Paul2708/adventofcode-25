from shared.paul2708.input_reader import *
from shared.paul2708.output import write

lines = read_plain_input(day=3, example=None)

def has_chars(l, a, b):
    if a not in l or b not in l:
        return False

    i = l.index(a)
    j = len(l) - 1 - l[::-1].index(b)

    if i < j:
        return True

    return False


c = 0

for l in lines:
    for i in range(99, 9, -1):
        a = str(i)

        if has_chars(l, a[0], a[1]):
            c += i
            break

print(c)