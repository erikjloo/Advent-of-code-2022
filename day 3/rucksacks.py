# PART A: Find common item in first half and second half of each line

score = 0
with open("day 3/input.txt") as f:
    for line in f.readlines():
        mid = len(line)//2
        c = set(line[:mid]).intersection(line[mid:]).pop()
        score += ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27
print(score)

# PART B: Find common item in each set of 3 lines

score = 0
with open("day 3/input.txt") as f:
    lines = f.read().splitlines()
    for i in range(len(lines)//3):
        d = set(lines[3*i]).intersection(lines[3*i+1], lines[3*i+2]).pop()
        score += ord(d) - ord('a') + 1 if d.islower() else ord(d) - ord('A') + 27
print(score)