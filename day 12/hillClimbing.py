from memory_profiler import profile

class HillClimb:

    def __init__(self, filename: str) -> None:
        self.grid = []
        self.grid2 = []
        with open(filename) as f:
            for i, line in enumerate(f.read().splitlines()):
                if line.count('S'):
                    self.end = (i, line.find('S'))
                    line = line.replace('S', 'a')
                if line.count('E'):
                    self.start = (i, line.find('E'))
                    line = line.replace('E', 'z')
                self.grid.append([ord(letter) for letter in list(line)])
                self.grid2.append(list(line))
        self.nrow = len(self.grid)
        self.ncol = len(self.grid[0])

    @profile
    def BFS(self):
        self.visited = {self.start: self.start}
        q = [self.start]
        while len(q):
            ic, jc = q.pop(0)
            for i, j in self.neighbors(ic, jc):
                if (i, j) in self.visited:
                    continue
                if (self.grid[i][j] - self.grid[ic][jc]) < -1:
                    continue
                q.append((i, j))
                self.visited[(i, j)] = (ic, jc)
                if self.grid2[i][j] == "a": # Part B
                    return (i, j)
                # if (i, j) == self.end: # Part A
                    # return (i, j)
        return self.start

    def neighbors(self, ic: int, jc: int):
        return set([(ic, max(jc-1, 0)), 
                    (ic, min(jc+1, self.ncol-1)), 
                    (max(ic-1, 0), jc),
                    (min(ic+1, self.nrow-1), jc)])

    def shortest_path(self) -> int:
        path = [(idx := self.BFS())]
        while idx in self.visited and idx != self.start:
            idx = self.visited[idx]
            path.append(idx)
        return len(path)-1

if __name__ == "__main__":
    hc = HillClimb("day 12/input.txt")
    print(hc.shortest_path())
    