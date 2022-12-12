import re
import numpy as np
import logging


def factors(nr: int) -> set:
    i = 2
    factors = set()
    while i <= nr:
        if (nr % i) == 0:
            factors.add(i)
            nr = nr / i
        else:
            i = i + 1
    return factors

class Monkeys:

    class Monkey:

        def __init__(self):
            self.inspected: list = 0
            self.items: list = []
            self.dest: list = []
            self.sign: str = ""
            self.param: int = 0
            self.params: set = {}
            self.factor: int = 0
            self.factors: set = {}
            # self.operation = lambda x: x
            # self.test = lambda x: x

    ops = {"+": (lambda x, y: x + y),
           "-": (lambda x, y: x - y),
           "*": (lambda x, y: x * y),
           "/": (lambda x, y: x / y)}

    def __init__(self, filename: str) -> None:
        pattern = re.compile("\d+")
        self.monkeys = []
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
                        self.monkeys[-1].params = factors(int(b))
                elif line.strip().startswith("Test"):
                    self.monkeys[-1].factor = int(pattern.findall(line)[0])
                    self.monkeys[-1].factors = factors(int(pattern.findall(line)[0]))
                    self.monkeys[-1].factors_params = self.monkeys[-1].factors.union(self.monkeys[-1].params)
                elif line.strip().startswith("If"):
                    self.monkeys[-1].dest[line.count("true")] = int(pattern.findall(line)[0])

    def rounds(self, nrounds: int = 20) -> None:
        for i in range(nrounds):
            # if (i % 100 == 0):
            #     print("Round %i" % i)
            #     self.print_inspected()
            self.round()
            # self.print_items()

    def round(self) -> None:
        for monkey in self.monkeys:
            # logging.debug("Monkey {}:".format(i))
            monkey.inspected += len(monkey.items)
            while len(monkey.items):
                item = monkey.items.pop(0)
                logging.debug("  Item with worry level {}".format(item))
                item = self.ops[monkey.sign](item, monkey.param if monkey.param else item)

                condition = False
                if monkey.sign == "+":
                    # item += (monkey.param if monkey.param else item)
                    condition = len(factors(item).intersection(monkey.factors)) == len(monkey.factors)
                elif monkey.sign == "*":
                    # item *= (monkey.param if monkey.param else item)

                    # print(factors(item).union(monkey.params))
                    # print(monkey.factors)
                    # print(len(factors(item).union(monkey.params).intersection(monkey.factors)))
                    # print(len(monkey.factors))
                    condition = len(factors(item).union(monkey.params).intersection(monkey.factors)) == len(monkey.factors)
                logging.debug("  Item worry level updated to {}".format(item))
                # item = item // 3
                # logging.debug("  Item worry level updated to {}".format(item))

                # condition = ((item % monkey.factor) == 0) or ((monkey.param % monkey.factor) == 0)
                # condition = (item % monkey.factor) == 0
                # logging.debug("  Item {} divisible by {}".format("" if condition else "not", monkey.factor))
                self.monkeys[monkey.dest[condition]].items.append(item)
                logging.debug("  Item {} sent to monkey {}".format(item, monkey.dest[condition]))

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
    monkeys = Monkeys("day 11/simple.txt")
    monkeys.rounds(20)
    monkeys.print_inspected()
    print(monkeys.monkey_business())
    # print(10000/100)