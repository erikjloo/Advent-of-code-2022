import re
import numpy as np
import copy

pattern = re.compile('\d+')
with open("day 5/input.txt") as f:
    lines = f.readlines()
    pos = int(np.where([pattern.search(line) is not None for line in lines])[0][0])
    stack_labels = pattern.findall(lines[pos])
    stacks = {stack_label:[] for stack_label in stack_labels}
    for i in range(pos-1, -1, -1):
        for stack_label, stack_pos in zip(stack_labels, pattern.finditer(lines[pos])):
            value = lines[i][stack_pos.start()]
            if value != ' ':
                stacks[stack_label].append(value)
    print(stacks)
    stacks2 = copy.deepcopy(stacks)
    stacks3 = copy.deepcopy(stacks)
    for i in range(pos+1, len(lines)):
        if a := pattern.findall(lines[i]):
            stacks3[a[2]].extend(stacks3[a[1]][-int(a[0]):])
            del stacks3[a[1]][-int(a[0]):]
            queue = []
            for _ in range(int(a[0])):
                if len(stacks[a[1]]):
                    queue.append(stacks2[a[1]].pop())
                    stacks[a[2]].append(stacks[a[1]].pop())
            for _ in range(int(a[0])):
                stacks2[a[2]].append(queue.pop())

    print(''.join([stacks[j].pop() for j in stacks]))
    print(''.join([stacks2[j].pop() for j in stacks]))
    print(''.join([stacks3[j].pop() for j in stacks]))



