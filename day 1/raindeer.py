import numpy as np

i = 0
amount = [0]

with open("day 1/input.txt") as f:
    for line in f.read().splitlines():
        if line == "":
            i += 1
            amount.append(0)
        else:
            amount[i] += int(line)

amount = np.sort(amount)
print(np.sum(amount[-3:]))

