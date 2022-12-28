import re

class Beacons:

    def __init__(self, filename: str, y: int) -> None:
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


if __name__ == "__main__":
    b = Beacons("day 15/simple.txt", 10)
    b = Beacons("day 15/input.txt", 2000000)
