import re
import math

class Beacons:

    # def __init__(self, filename: str, y: int) -> None:
    #     pattern = re.compile("-?\d+")
    #     ze_set = set()
    #     with open(filename) as f:
    #         for line in f.read().splitlines():
    #             sensor, beacon = line.split(":")
    #             xs, ys = [int(x) for x in pattern.findall(sensor)]
    #             xb, yb = [int(x) for x in pattern.findall(beacon)]
    #             d = abs(xs - xb) + abs(ys - yb)

    #             if ys - d <= y <= ys + d:
    #                 d2 = d - abs(y - ys)
    #                 for ble in range(-d2, d2):
    #                     ze_set.add(xs + ble)
    #     print(len(ze_set))
    
    def __init__(self, filename: str) -> None:
        pattern = re.compile("-?\d+")
        ze_set = set()
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

                for bla in range(-d, d+1):
                    y = ys + bla
                    d2 = d - abs(y - ys)
                    for ble in range(-d2, d2+1):
                        ze_set.add((xs + ble, y))

        la = 0
        for x in range(x_min, x_max):
            for y in range(y_min, y_max):
                la += 1  
                if (x, y) not in ze_set:
                    print(x*4000000 + y)
                    return
        # print(len(ze_set))  
# 
if __name__ == "__main__":
    # b = Beacons("day 15/simple.txt", 10)
    # b = Beacons("day 15/input.txt", 2000000)
    # b = Beacons("day 15/simple.txt", 20, 20)
    b = Beacons("day 15/input.txt")
