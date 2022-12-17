# PART A: Find subset count (first range covers second range or vice-versa)
# PART B: FInd overlap count

subset_count = 0
overlap_count = 0
with open("day 4/input.txt") as f:
    for line in f.read().split():
        a, b = line.split(',')
        a = [int(x) for x in a.split('-')]
        b = [int(x) for x in b.split('-')]
        # Modified as per Mishko's superior code
        subset_count += (a[0] <= b[0] and b[1] <= a[1]) or (b[0] <= a[0] and a[1] <= b[1])
        overlap_count += (a[0] <= b[0] <= a[1]) or (b[0] <= a[0] <= b[1])

print(subset_count)
print(overlap_count)
