

class HillClimb:

    def __init__(self, filename: str) -> None:
        self.grid = []
        self.grid2 = []
        with open(filename) as f:
            for i, line in enumerate(f.read().splitlines()):
                if line.count('S'):
                    self.start = (i, line.find('S'))
                    line = line.replace('S', 'a')
                if line.count('E'):
                    self.end = (i, line.find('E'))
                    line = line.replace('E', 'z')
                self.grid.append([ord(letter) for letter in list(line)])
                self.grid2.append(list(line))
        self.nrow = len(self.grid)
        self.ncol = len(self.grid[0])

    def BFS(self):
        self.visited = {self.start: self.start}
        queue = [self.start]
        while len(queue) and queue[0] != self.end:
            ic, jc = queue.pop(0)
            for i, j in ([(ic, jc-1), (ic, jc+1), (ic-1, jc), (ic+1, jc)]):
                if (i, j) in self.visited:
                    continue
                if not(0 <= i < self.nrow and 0 <= j < self.ncol):
                    continue
                if abs(self.grid[i][j] - self.grid[ic][jc]) > 1:
                    continue
                    # visited.add((i, j))
                    # print(abs(self.grid[i][j] - self.grid[ic][jc]))
                queue.append((i, j))
                self.visited[(i, j)] = (ic, jc)
                print(self.grid2[i][j])
                    # print(self.grid2[i][j])
                    # print((i, j) == self.end)
                if (i, j) == self.end:
                    return (i, j)
        # return self.start
    
    def shortest_path(self) -> int:
        i, j = self.BFS()
        # print(len(self.visited))
        path = [(i, j)]
        while (i, j) != self.start:
            (i, j) = self.visited[(i, j)]
            path.append((i, j))
        return len(path)-1

if __name__ == "__main__":
    hc = HillClimb("day 12/simple.txt")
    print(hc.shortest_path())
    