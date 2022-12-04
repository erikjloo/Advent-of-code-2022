

score = 0
val2score = {0:3, 1:6, 2:0}

with open("day 2/input.txt") as f:
    for line in f.readlines():
        a = ord(line[0]) - ord('A') # a = 0, 1 or 2
        b = ord(line[2]) - ord('X') # b = 0, 1 or 2
        score += val2score[(b - a)%3] + b + 1 # higher number wins. negative wraps around to 2

print(score)

# The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

# In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.


score = 0
val2score = {0:3, 1:6, 2:0}

with open("day 2/input.txt") as f:
    for line in f.readlines():
        a = ord(line[0]) - ord('A') # a = 0, 1 or 2
        action = ord(line[2]) - ord('Y') # actions is -1 (lose), 0 (draw), or 1(win)
        b = ((a + action) % 3) # b is lower to lose, same if draw, higher if win
        score += val2score[(b - a)%3] + b + 1

print(score)
