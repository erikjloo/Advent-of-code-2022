from enum import Enum
import numpy as np
import math
import time

class Material(Enum):
    STONE = 1
    SAND = 2

class Reservoir:

    def __init__(self, filename: str) -> None:
        self.part_a : bool = True
        self.grid : dict = {}
        self.min_x : int = math.inf
        self.max_x : int = -math.inf
        self.min_y : int = math.inf
        self.max_y : int = -math.inf

        with open(filename) as f:
            for line in f.read().splitlines():
                path: list = [self.read_coord(c) for c in line.split("->")]
                self.populate_path(path)
        self.bedrock = self.max_y + 2

    def read_coord(self, coord: str) -> tuple:
        """ Reads the coordinate AND updates the the bounds """
        x, y = [int(x.strip()) for x in coord.split(",")]
        self.update_bounds(x, y)
        return (x, y)

    def update_bounds(self, x: int, y: int) -> None:
        self.min_x = min(self.min_x, x)
        self.max_x = max(self.max_x, x)
        self.min_y = min(self.min_y, y)
        self.max_y = max(self.max_y, y)

    def populate_path(self, path: list) -> None:
        """ Fills in coords traversed by path """
        for i in range(len(path)-1):
            c1 = np.array(path[i])
            c2 = np.array(path[i+1])
            dir = np.sign(c2 - c1)
            c = c1
            for _ in range(max(abs(c2-c1))+1):
                self.grid[tuple(c)] = Material.STONE
                c += dir

    def drop_sand(self, part_a: bool = True) -> int:
        """ Drops sand units until sand falls of the edge """
        start = time.time()
        for key in list(self.grid.keys()):
            if self.grid[key] == Material.SAND:
                del self.grid[key]   

        self.part_a = part_a
        counter: int = 0
        while self.drop_sand_unit():
            counter +=1
        end = time.time()
        print("Time: {} s.".format(end-start))
        return counter + (not self.part_a)

    def drop_sand_unit(self, x0: int = 500, y0: int = 0) -> bool:
        """ Drops a unit of sand until it (a) falls thru or (b) settles down 
            Returns true if more sand can be poured """
        x, y = x0, y0
        while True:
            if self.part_a and y > self.max_y: # Check if falling thru max_y
                return False
            elif not self.part_a and y == (self.bedrock-1):
                self.grid[(x, y)] = Material.SAND
                self.update_bounds(x, y) # for printing
                return True
            elif (x, y+1) not in self.grid: # Check below
                y += 1
            elif (x-1, y+1) not in self.grid: # Check left
                x -= 1
                y += 1
            elif (x+1, y+1) not in self.grid: # Check right
                x += 1
                y += 1
            else: # All checks fail -> Sand has settled
                self.grid[(x, y)] = Material.SAND
                self.update_bounds(x, y) # for printing
                return not (x == x0 and y == y0) #x != x0 or y != y0

    def print(self) -> None:
        grid = [["." for _ in range(self.max_x - self.min_x+1)] for _ in range(self.max_y - self.min_y+1)]
        for x, y in self.grid:
            grid[y - self.min_y][x - self.min_x] = "#" if self.grid[(x, y)] is Material.STONE else "o"
        for line in grid:
            print("".join(line))

if __name__ == "__main__":
    r = Reservoir("day 14/input.txt")
    print(r.drop_sand(part_a=True))
    print(r.drop_sand(part_a=False))
    # r.print()