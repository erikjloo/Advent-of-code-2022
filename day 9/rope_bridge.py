import numpy as np
# from numpy.linalg import norm

class RopeBridge:

    NROW: int = 5
    NCOL: int = 6
    __tail_count: int = 1

    def __init__(self, filename: str, tail_count: int = 1) -> None:
        self.tail_count = tail_count
        with open(filename) as f:
            self.moves = list(f.read().splitlines())

    @property
    def tail_count(self) -> int:
        return self.__tail_count

    @tail_count.setter
    def tail_count(self, tail_count: int) -> None:
        self.visited = set()
        self.__tail_count = tail_count
        self.Rope = [np.array([0, 0]) for _ in range(self.__tail_count+1)]

    def execute_moves(self) -> None:
        for move in self.moves:
            self.execute_move(move)

    def execute_move(self, move: str) -> None:
        direction, count = move.split()
        dx = (direction == "R") - (direction == "L")
        dy = (direction == "U") - (direction == "D")
        for _ in range(int(count)):
            self.Rope[0] += np.array([dy, dx])
            self.move_tail()
            # self.print_state()

    def move_tail(self) -> None:
        for i in range(1, self.tail_count+1):
            delta = self.Rope[i-1] - self.Rope[i]
            # self.Rope[i] += np.sign(delta)*int(norm(delta)//2)
            self.Rope[i] += np.sign(delta)*((delta[0]**2+delta[1]**2) > 2)
        self.visited.add(tuple(self.Rope[-1]))

    def print_visited(self) -> None:
        x = [pos[0] for pos in self.visited]
        y = [pos[1] for pos in self.visited]

        for row in range(max(x), min(x)-1, -1):
            line = ""
            for col in range(min(y), max(y)):
                line += "#" if (row, col) in self.visited else "."
            print(line)
        print("")

    def print_state(self) -> None:
        for row in range(self.NROW-1, -1, -1):
            line = ""
            for col in range(self.NCOL):
                for elem in range(self.tail_count+1):
                    if all((self.Rope[elem]) == np.array([row, col])):
                        line += str(elem)
                        break
                else:
                    line += "."
            print(line.replace("0", "H"))
        print("")

if __name__ == "__main__":
    rb = RopeBridge("day 9/input.txt", 1)
    rb.execute_moves()
    print(len(rb.visited))
    # rb.print_visited()

    rb.tail_count = 9
    rb.execute_moves()
    print(len(rb.visited))
    # rb.print_visited()