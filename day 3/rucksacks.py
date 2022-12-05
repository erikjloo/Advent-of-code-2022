score = 0
with open("day 3/input.txt") as f:
    for line in f.readlines():
        mid = len(line)//2
        a = line[:mid]
        b = line[mid:]
        c = set(a).intersection(b).pop()
        score += ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27
print(score)

# As you finish identifying the misplaced items, the Elves come to you with another issue.
# For safety, the Elves are divided into groups of three. Every Elf carries a badge that 
# identifies their group. For efficiency, within each group of three Elves, the badge is 
# the only item type carried by all three Elves. That is, if a group's badge is item type B, 
# then all three Elves will have item type B somewhere in their rucksack, and at most two of 
# the Elves will be carrying any other item type.

# The problem is that someone forgot to put this year's updated authenticity sticker on the badges. 
# All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.
# Additionally, nobody wrote down which item type corresponds to each group's badges. 
# The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

# Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

score = 0
with open("day 3/input.txt") as f:
    lines = f.read().splitlines()
    for i in range(len(lines)//3):
        d = set(lines[3*i]).intersection(lines[3*i+1], lines[3*i+2]).pop()
        score += ord(d) - ord('a') + 1 if d.islower() else ord(d) - ord('A') + 27
print(score)