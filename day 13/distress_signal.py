import json
from typing import Union
import random

class DistressSignal:

    def __init__(self, filename: str) -> None:
        with open(filename) as f:
            self.lines = f.read().splitlines()

    def part_a(self) -> int:
        self.pairs = [[]]
        for line in self.lines:
            if len(line):
                self.pairs[-1].append(json.loads(line))
            elif len(self.pairs[-1]):
                self.pairs.append([])

        correct_order = []
        totes = 0
        for i, pair in enumerate(self.pairs):
            if DistressSignal.compare(pair[0], pair[1]):
                correct_order.append(i+1)
                totes += i+1
        # print(correct_order)
        return totes

    def part_b(self) -> int:
        self.packets = [[[2]], [[6]]]
        for line in self.lines:
            if len(line):
                self.packets.append(json.loads(line))
        self.indices = DistressSignal.quick_sort(self.packets, 0, len(self.packets)-1)
        return (self.indices.index(0)+1)*(self.indices.index(1)+1)

    @staticmethod
    def quick_sort(ls, left: int, right: int, idx: list = None) -> list[int]:

        if idx is None:
            idx = list(range(len(ls)))

        # Choose pivot
        p = random.randint(left, right)
        pivot = ls[p]

        # Swap pivot with first element of sub-array
        ls[left], ls[p] = ls[p], ls[left]
        idx[left], idx[p] = idx[p], idx[left]

        # i keeps track of last element smaller than pivot
        i = j = left
        while j != right:
            j += 1
            if DistressSignal.compare(ls[j], pivot): # j smaller than pivot
                # Last element smaller than pivot is now one more to the right
                i += 1
                # Switch jth element with first element bigger than the pivot
                ls[j], ls[i] = ls[i], ls[j]                
                idx[j], idx[i] = idx[i], idx[j]

        # Swap the pivot with the last element smaller than the pivot -> i becomes the pivot
        ls[left], ls[i] = ls[i], ls[left]
        idx[left], idx[i] = idx[i], idx[left]

        if (i != left): # quick_sort to left of pivot
            DistressSignal.quick_sort(ls, left, i-1, idx)

        if (i != right): # quick_sort to right of pivot
            DistressSignal.quick_sort(ls, i+1, right, idx)
        
        return idx

    @staticmethod
    def compare(a: Union[int, list], b: Union[int, list]) -> bool:
        if isinstance(a, int) and isinstance(b, int):
            # print("Compare {} vs {}".format(a,b))
            return a < b 
        if isinstance(a, int) and isinstance(b, list):
            return DistressSignal.compare([a], b)
        if isinstance(a, list) and isinstance(b, int):
            return DistressSignal.compare(a, [b])
        if isinstance(a, list) and isinstance(b, list):
            # print("Compare {} vs {}".format(a,b))
            for i in range(max(len(a), len(b))):
                if len(a) <= i: # a runs out of elements
                    # print("Left side smaller")
                    return True
                if len(b) <= i:
                    # print("Right side smaller")
                    return False
                if DistressSignal.compare(a[i], b[i]):
                    return True
                if DistressSignal.compare(b[i], a[i]):
                    return False
        return False

if __name__ == "__main__":
    ds = DistressSignal("day 13/input.txt")
    print(ds.part_a())
    print(ds.part_b())
