import re
import numpy as np
import copy

pattern = re.compile('\d+')
with open("day 5/input.txt") as f:
    lines = f.readlines()
    pos = int(np.where([pattern.search(line) is not None for line in lines])[0][0])

    # Read the stack labels and positions
    stack_labels = pattern.findall(lines[pos])
    stack_positions = [it.start() for it in pattern.finditer(lines[pos])]

    # Initialise empty stacks
    stacks = {stack_label:[] for stack_label in stack_labels}

    # Fill stacks
    for line in reversed(lines[:pos]):
        for stack_label, stack_pos in zip(stack_labels, stack_positions):
            if (letter := line[stack_pos]).isalpha():
                stacks[stack_label].append(letter)

    stacks2 = copy.deepcopy(stacks)

    # Iterate over remaining lines
    for line in lines[pos+1:]:

        # Follow instruction (if it exists)
        if a := pattern.findall(line):

            # Get no. of cranes to be moved
            a0 = min(int(a[0]), len(stacks[a[1]])) 

            # Crane mover 9001
            stacks2[a[2]].extend(stacks2[a[1]][-a0:])
            del stacks2[a[1]][-a0:]

            # Crane mover 9000
            for _ in range(a0):
                stacks[a[2]].append(stacks[a[1]].pop())

    print(''.join([stacks[j].pop() for j in stacks]))
    print(''.join([stacks2[j].pop() for j in stacks]))



