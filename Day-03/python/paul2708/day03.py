from requests.cookies import remove_cookie_by_name

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


def smallest_digets(l):
    nums = list(map(int, l))
    nums = sorted(nums)
    return nums[:3]


def remove_index(S, Index):
    return S[:Index] + S[Index + 1:]


def next_nums(l, i, rems):
    res = []
    for k in range(1, rems + 1):
        if i + k < len(l):
            res.append(int(l[i + k]))
    return res


total_removals = len(lines[0]) - 12

ss = 0
for l in lines:
    removals = 0

    r = ""

    for i in range(len(l)):
        if removals == total_removals:
            r += l[i]
            continue

        current = int(l[i])
        next_n = next_nums(l, i, total_removals - removals)
        m = max(next_n + [current])

        if m == current:
            # print(f"Keep {current}")
            r += l[i]
        else:
            removals += 1

    print(l, r[:12])
    ss += int(r[:12])

print(ss)
