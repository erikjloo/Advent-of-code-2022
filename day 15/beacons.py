import re
import math
import time

class Beacons:

    def __init__(self) -> None:
        pass

    def part_a(self, filename: str, y: int) -> None:
        start = time.time()
        pattern = re.compile("-?\d+")
        ze_set = set()
        with open(filename) as f:
            for line in f.read().splitlines():
                sensor, beacon = line.split(":")
                xs, ys = [int(x) for x in pattern.findall(sensor)]
                xb, yb = [int(x) for x in pattern.findall(beacon)]
                d = abs(xs - xb) + abs(ys - yb)

                if ys - d <= y <= ys + d:
                    d2 = d - abs(y - ys)
                    for ble in range(-d2, d2):
                        ze_set.add(xs + ble)
        print(len(ze_set))
        end = time.time()
        print("Time consumed in working: ", end - start)
    
    def part_a_2(self, filename: str, y: int) -> None:
        start = time.time()
        pattern = re.compile("-?\d+")
        ze_list = []
        x_min = math.inf
        y_min = math.inf
        x_max = -math.inf
        y_max = -math.inf
        with open(filename) as f:
            for line in f.read().splitlines():
                sensor, beacon = line.split(":")
                xs, ys = [int(x) for x in pattern.findall(sensor)]
                xb, yb = [int(x) for x in pattern.findall(beacon)]
                d = abs(xs - xb) + abs(ys - yb)

                x_min = min(x_min, xs, xb)
                y_min = min(y_max, ys, yb)
                x_max = max(x_max, xs, xb)
                y_max = max(y_max, ys, yb)

                ze_list.append((xs, ys, d))

        # Consider |xs - x| + |ys - y| <= d
        # Rearranging: x = xs ± |d - |ys - y|| if d - |ys - y| > 0 
        #
        le_dict = {}
        for xs, ys, d in ze_list:
            if (delta := d - abs(ys - y)) > 0:
                a, b = xs - abs(delta), xs + abs(delta)
                le_dict[a] = b

        A = []
        for a in sorted(le_dict):
            b = le_dict[a]
            if len(A):
                for bala in A:
                    if bala[0] <= a <= bala[1]:
                        bala[1] = max(bala[1], b)
                        break
                else:
                    A.append([a, b])
            else:
                A = [[a, b]]

        out = 0
        for bala in A:
            out += bala[1] - bala[0]
        print(out)
            # get the ranges of x that cannot contain stuff
        # out = set()
        # for x in range(x_min, x_max):
        #     if any([abs(xs - x) + abs(ys - y) < d for xs, ys, d in ze_list]):
        #         out.add(x)
        # print(len(out))
        end = time.time()
        print("Time consumed in working: ",end - start)
    # def __init__(self, filename: str) -> None:
    #     pattern = re.compile("-?\d+")
    #     ze_set = set()
    #     x_min = math.inf
    #     y_min = math.inf
    #     x_max = -math.inf
    #     y_max = -math.inf
    #     with open(filename) as f:
    #         for line in f.read().splitlines():
    #             sensor, beacon = line.split(":")
    #             xs, ys = [int(x) for x in pattern.findall(sensor)]
    #             xb, yb = [int(x) for x in pattern.findall(beacon)]
    #             d = abs(xs - xb) + abs(ys - yb)

    #             x_min = min(x_min, xs)
    #             y_min = min(y_max, ys)
    #             x_max = max(x_max, xs)
    #             y_max = max(y_max, ys)

                
    #             for bla in range(-d, d+1):
    #                 y = ys + bla
    #                 d2 = d - abs(y - ys)
    #                 for ble in range(-d2, d2+1):
    #                     ze_set.add((xs + ble, y))

    #     for x in range(x_min, x_max):
    #         for y in range(y_min, y_max):
    #             if (x, y) not in ze_set:
    #                 print(x*4000000 + y)
    #                 return
    #     print(len(ze_set))  

    def part_b(self, filename: str) -> None:
        start = time.time()
        pattern = re.compile("-?\d+")
        ze_list = []
        x_min = math.inf
        y_min = math.inf
        x_max = -math.inf
        y_max = -math.inf
        with open(filename) as f:
            for line in f.read().splitlines():
                sensor, beacon = line.split(":")
                xs, ys = [int(x) for x in pattern.findall(sensor)]
                xb, yb = [int(x) for x in pattern.findall(beacon)]
                d = abs(xs - xb) + abs(ys - yb)

                x_min = min(x_min, xs)
                y_min = min(y_max, ys)
                x_max = max(x_max, xs)
                y_max = max(y_max, ys)

                ze_list.append((xs, ys, d))

        for y in range(y_min, y_max):
            
            for x in range(x_min, x_max):
                bo = [abs(xs - x) + abs(ys - y) > d for xs, ys, d in ze_list]
                if all(bo):
                    print(x*4000000 + y)
                    end = time.time()
                    print("Time consumed in working: ",end - start)
                    return

if __name__ == "__main__":
    # b = Beacons("day 15/simple.txt", 10)
    # b = Beacons("day 15/input.txt", 2000000)
    # b = Beacons("day 15/simple.txt", 20, 20)
    b = Beacons()
    b.part_a("day 15/simple.txt", 10)
    b.part_a_2("day 15/simple.txt", 10)
    b.part_a("day 15/input.txt", 2000000)
    b.part_a_2("day 15/input.txt", 2000000)
    b.part_b("day 15/simple.txt")

    # b.part_a_2("day 15/input.txt", 10)

    
