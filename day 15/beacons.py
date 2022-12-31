import re
import math
import time

def clamp(x : int, x_min : int, x_max : int) -> int:
    return min(max(x, x_min), x_max)

class Beacons:

    def __init__(self, filename) -> None:
        start = time.time()
        pattern = re.compile("-?\d+")
        self.diamonds = list()
        self.x_min = math.inf
        self.x_max = -math.inf
        self.y_min = math.inf
        self.y_max = -math.inf
        with open(filename) as f:
            for line in f.read().splitlines():
                sensor, beacon = line.split(":")
                xs, ys = [int(x) for x in pattern.findall(sensor)]
                xb, yb = [int(x) for x in pattern.findall(beacon)]
                d = abs(xs - xb) + abs(ys - yb)
                self.diamonds.append((xs, ys, d))
                self.x_min = min(self.x_min, xs)
                self.x_max = max(self.x_max, xs)
                self.y_min = min(self.y_max, ys)
                self.y_max = max(self.y_max, ys)
        self.diamonds.sort(key = lambda x: x[0] - x[2])
        end = time.time()
        print("Data read.\n  Time: {} s.".format(end-start))

    def find_intersects(self) -> list:
        y = set()
        for i, (xs1, ys, d) in enumerate(self.diamonds):
            yt1, yb1 = (ys + d + 1), (ys - d - 1)
            xl1, xr1 = (xs1 + d + 1), (xs1 - d - 1)

            for xs2, ys, d in self.diamonds[i+1:]:
                yt2, yb2 = (ys + d + 1), (ys - d - 1)
                xl2, xr2 = (xs2 + d + 1), (xs2 - d - 1)
                dx = abs(xs2 - xs1)
                y.add((yb1 + yt2 + dx)//2)
                y.add((yb1 + yt2 - dx)//2)
                y.add((yb2 + yt1 + dx)//2)
                y.add((yb2 + yt1 - dx)//2)
                y.add((yt1 + yt2 + dx)//2)
                y.add((yt1 + yt2 - dx)//2)
                y.add((yb1 + yb2 + dx)//2)
                y.add((yb1 + yb2 - dx)//2)
        return y

    def part_a(self, y: int) -> None:
        """ Returns the number of positions without beacons at the given y-coordinate """
        start = time.time()
        out = sum([xr - xl for xl, xr in self.x_coordinate_pairs(y)])
        end = time.time()
        print("Part a: {} unoccupied positions.\n  Time: {} s".format(out, end - start))

    def part_b(self) -> None:
        start = time.time()
        # for y in range(self.y_min, self.y_max+1):
        for y in self.find_intersects():
            if y < self.y_min or y > self.y_max:
                continue
            if len(x := self.x_coordinate_pairs(y)) > 1:
                out = (x[0][1] + x[1][0])//2 *4000000 + y
                end = time.time()
                print("Part b: {} unoccupied positions.\n  Time: {} s".format(out, end - start))
                return

    def x_coordinate_pairs(self, y: int) -> list:
        """ Returns list of x-coordinate pairs denoting the start and the end
            of regions without beacons at the given y-coordinate """
        # The region without beacons is defined by the inequality:
        #     |xs - x| + |ys - y| <= d
        # Rearranging:
        #     x = xs ± (d - |ys - y|) if d - |ys - y| > 0 
        # Let dx = d - |ys - y|:
        #     x = xs ± dx if dx > 0
        # We store the left and right x in a list of pairs:
        #     [(x_left, x_right)]
        x = [(xs-dx, xs+dx) for xs, ys, d in self.diamonds if (dx := d-abs(ys-y)) > 0]
        # Merge overlaping x-coordinate pairs.
        # (1) Sort x by the x_left and iterate over each sorted x-coordinate pair.
        # (2) Check if the current x_left is within previous [x_left, x_right]
        #     (a) Merge if true
        #     (b) Append new range if false
        merged = []
        for a, b in sorted(x): # Iterate over each sorted x-coordinate pair
            if len(merged):
                for x_pair in merged:
                    if x_pair[0] <= a <= x_pair[1]: # Merge if overlaping any range in merged
                        x_pair[1] = max(x_pair[1], b)
                        break
                else: # otherwise append new range to merged
                    merged.append([a, b])
            else:
                merged.append([a, b])
        return merged

    def y_coordinate_pairs(self, x: int) -> list:
        """ Returns list of y-coordinate pairs denoting the start and the end
            of regions without beacons at the given x-coordinate """
        y = [(ys-abs(dy), ys+abs(dy)) for xs, ys, d in self.diamonds if (dy := d-abs(xs-x)) > 0]
        merged = []
        for a, b in sorted(y): # Iterate over each sorted x-coordinate pair
            if len(merged):
                for y_pair in merged:
                    if y_pair[0] <= a <= y_pair[1]: # Merge if overlaping any range in merged
                        y_pair[1] = max(y_pair[1], b)
                        break
                else: # otherwise append new range to merged
                    merged.append([a, b])
            else:
                merged.append([a, b])
        return merged

if __name__ == "__main__":
    # b = Beacons("day 15/simple.txt")
    # b.part_a(10)
    # b.part_b()
    b = Beacons("day 15/input.txt")
    b.part_a(2000000)
    b.part_b()