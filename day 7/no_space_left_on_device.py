
class Node:
    def __init__(self, new_key: str = None, new_data: int = None, new_parent):
        self.key = new_key
        self.data = new_data
        self.parent = new_parent
        self.children = []

class Tree:
    def __init__(self):
        self.root = Node("/")
        self.pointer = self.root
    
    # def 
    

def read_dir(filename : str) -> None:
    tree = Tree()
    tree.push("/")
    with open(filename) as f:
        lines = f.read().split()
    for line in lines:
        a, b, c = line.split()
        if b == "cd" and c == "/":
            tree.move_pointer("/")
        elif b == "cd" and c == "..":
            tree.go_to_parent()
        elif b == "cd":
            tree.add_child(c)
            tree.go_to_child(c)
        elif a.isnumeric():
            tree.add_child(b, a)

    tree.print()

if __name__ == "__main__":
    read_dir("day 7/simple.txt")