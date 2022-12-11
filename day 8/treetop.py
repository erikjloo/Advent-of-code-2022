# PART A: Find number of "visible" trees
# visible: All trees to the left, right, top or bottom are shorter (don't obstruct the view)

class TreeGrid:

    def __init__(self, filename : str):
        self.grid = []
        self.tree_set = set()
        with open(filename) as f:
            for line in f.read().splitlines():
                self.grid.append([int(char) for char in line])
        self.nrow = len(self.grid)
        self.ncol = len(self.grid[0])

    def check_visible(self) -> None:
        for i in range(self.nrow): # row
            max_height = -1
            for j in range(self.ncol): # col
                if self.grid[i][j] > max_height:
                    self.tree_set.add((i, j))
                    max_height = self.grid[i][j]

            max_height = -1
            for j in range(self.ncol-1, -1, -1): # col from the right to the left
                if self.grid[i][j] > max_height:
                    self.tree_set.add((i, j))
                    max_height = self.grid[i][j]

        for j in range(self.ncol):
            max_height = -1
            for i in range(self.nrow):
                if self.grid[i][j] > max_height:
                    self.tree_set.add((i, j))
                    max_height = self.grid[i][j]

            max_height = -1
            for i in range(self.nrow-1, -1, -1):
                if self.grid[i][j] > max_height:
                    self.tree_set.add((i, j))
                    max_height = self.grid[i][j]

        # print([[self.grid[i][j] if (i, j) in self.tree_set else 0 for j in range(self.ncol)] for i in range(self.nrow)])
        print(len(self.tree_set))
    
    def max_value(self) -> None:
        max_val = 0
        for i in range(1, self.nrow-1):
            for j in range(1, self.ncol-1):
                curr_height = self.grid[i][j]
                a = 0
                for i2 in range(i-1, -1, -1):
                    a += 1
                    if self.grid[i2][j] >= curr_height:
                        break
                b = 0
                for i2 in range(i+1, self.nrow):
                    b += 1
                    if self.grid[i2][j] >= curr_height:
                        break
                c = 0
                for j2 in range(j-1, -1, -1):
                    c += 1
                    if self.grid[i][j2] >= curr_height:
                        break
                d = 0
                for j2 in range(j+1, self.ncol):
                    d += 1
                    if self.grid[i][j2] >= curr_height:
                        break

                max_val = max(max_val, a*b*c*d)

        print(max_val)

if __name__ == "__main__":
    t = TreeGrid("day 8/input.txt")
    t.check_visible()
    t.max_value()