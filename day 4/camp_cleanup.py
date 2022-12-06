
subset_count = 0
overlap_count = 0
with open("day 4/input.txt") as f:
    for line in f.read().split():
        a, b = line.split(',')
        a1, a2 = a.split('-')
        b1, b2 = b.split('-')
        ra = set(range(int(a1), int(a2) + 1))
        rb = set(range(int(b1), int(b2) + 1))
        subset_count += len(ra.intersection(rb)) == min(len(ra), len(rb))
        overlap_count += len(ra.intersection(rb)) > 0 
print(subset_count)
print(overlap_count)
