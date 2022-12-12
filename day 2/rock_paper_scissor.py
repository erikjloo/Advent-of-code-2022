# PART A: 
# A, B, C are rock, paper, scissor
# X, Y, Z are rock, paper, scissor
# Win is 6, tie is 3, lose is 0. 
# Rock is 1, paper is 2, scissor is 3.
# E.g. Win with Rock is 6 + 1 = 7

score = 0
val2score = {0:3, 1:6, 2:0}

with open("day 2/input.txt") as f:
    for line in f.read().splitlines():
        a = ord(line[0]) - ord('A') # a = 0, 1 or 2 (rock, paper, scissor)
        b = ord(line[2]) - ord('X') # b = 0, 1 or 2 (rock, paper, scissor)
        score += val2score[(b - a)%3] + b + 1 # higher number wins. negative wraps around to 2

print(score)

# PART B:
# A, B, C are rock, paper scissor.
# X, Y, Z are lose, draw, win.
# Score is same as before

score = 0
val2score = {0:3, 1:6, 2:0}

with open("day 2/input.txt") as f:
    for line in f.read().splitlines():
        a = ord(line[0]) - ord('A') # a = 0, 1 or 2
        action = ord(line[2]) - ord('Y') # actions is -1 (lose), 0 (draw), or 1(win)
        b = ((a + action) % 3) # b is lower to lose, same if draw, higher if win
        score += val2score[(b - a)%3] + b + 1

print(score)
