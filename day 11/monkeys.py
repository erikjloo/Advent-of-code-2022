import re
import logging

class Monkeys:

    class Monkey:

        def __init__(self):
            self.inspected: list = 0
            self.items: list = []
            self.dest: list = []
            self.sign: str = ""
            self.param: int = 0
            self.factor: int = 0

    # ops = {"+": (lambda x, y: x + y),
    #        "-": (lambda x, y: x - y),
    #        "*": (lambda x, y: x * y),
    #        "/": (lambda x, y: x / y)}

    def __init__(self, filename: str) -> None:
        pattern = re.compile("\d+")
        self.monkeys = []
        self.factor = 1
        with open(filename) as f:
            for line in f.read().splitlines():
                if line.startswith("Monkey"):
                    self.monkeys.append(self.Monkey())
                elif line.strip().startswith("Starting"):
                    self.monkeys[-1].items = [int(match) for match in pattern.findall(line)]
                    self.monkeys[-1].dest = [-1, -1]
                elif line.strip().startswith("Operation"):
                    _, _, _, a, self.monkeys[-1].sign, b = line.split()
                    if b.isnumeric():
                        self.monkeys[-1].param = int(b)
                elif line.strip().startswith("Test"):
                    self.monkeys[-1].factor = int(pattern.findall(line)[0])
                    self.factor *= self.monkeys[-1].factor
                elif line.strip().startswith("If"):
                    self.monkeys[-1].dest[line.count("true")] = int(pattern.findall(line)[0])

    def rounds(self, nrounds: int = 20) -> None:
        for _ in range(nrounds):
            self.round()

    def round(self) -> None:
        for monkey in self.monkeys:
            monkey.inspected += len(monkey.items)
            while len(monkey.items):
                item = monkey.items.pop(0)
                if monkey.sign == "+":
                    item += (monkey.param if monkey.param else item)
                elif monkey.sign == "*":
                    item *= (monkey.param if monkey.param else item)

                # Trick provided by dgeoffri
                item -= (item // self.factor)*self.factor
                condition = (item % monkey.factor) == 0
                self.monkeys[monkey.dest[condition]].items.append(item)

    def print_items(self) -> None:
        for i, monkey in enumerate(self.monkeys):
            print("Monkey {}: {}". format(i, monkey.items))

    def print_inspected(self) -> None:
        for i, monkey in enumerate(self.monkeys):
            print("Monkey {} inspected items {} times". format(i, monkey.inspected))

    def monkey_business(self) -> int:
        temp = sorted([monkey.inspected for monkey in self.monkeys], reverse=True)
        return temp[0]*temp[1]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    monkeys = Monkeys("day 11/input.txt")
    monkeys.rounds(10000)
    monkeys.print_inspected()
    monkeys.print_items()
    print(monkeys.monkey_business())
    # print(10000/100)