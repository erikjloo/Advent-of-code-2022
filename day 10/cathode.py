# PART A: Calculate value in each cycle

values = [1]

with open("day 10/input.txt") as f:
    cycle = 0

    for line in f.read().splitlines():
        try:
            command, new_value = line.split()
            values.append(values[-1])
            values.append(values[-1] + int(new_value))
        except:
            values.append(values[-1])
            

totes = 0
for cycle in [20, 60, 100, 140, 180, 220]:
    totes += cycle*values[cycle-1]

print(totes)

# PART B: Print CRT output 
# Each cycle correspond to one "pixel"
# Pixel is drawn as # if value is within one pixel of current column number

i = 0
for row in range(6):
    line = ""
    for col in range(40):
        line += "#" if (col-1 <= values[i] <= col+1) else " "
        i += 1
    print(line)

