# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:35:38 2021

@author: ErikJ.GiesenLoo
"""

class Node:
    def __init__(self, new_key=None, new_data=None):
       self.key = new_key
       self.data = new_data # For implementation of dict/map
       self.left = None
       self.right = None
       self.height = 1

class Tree:
    def __init__(self):
        self.root = None

    def empty(self):
        return not self.root

    def insert(self, new_key : int, new_data = None):
        self.root = self.__find_and_insert(self.root, new_key, new_data)

    def __find_and_insert(self, node, new_key : int, new_data = None):
        if not node: # key not found
            node = Node(new_key)
        elif node.key == new_key:
            print("insert() used on existing key")
        elif new_key < node.key:
            node.left = self.__find_and_insert(node.left, new_key, new_data)
        else:
            node.right = self.__find_and_insert(node.right, new_key, new_data)
        self.__ensure_balance(node)
        return node

    def erase(self, key : int):
        self.__find_and_erase(self.root, key)
    
    def __find_and_erase(self, node, key):
        if not node:
            print("erase() used on non-existing key")
        elif node.key == key:
            node = self._erase(node)
        elif key < node.key:
            node.left = self.__find_and_erase(node.left, key)
        else:
            node.right = self.__find_and_erase(node.right, key)

    def __erase(self, node):
        if not node.left and not node.right: # node is a leaf
            node = None
        elif node.right and not node.left: # node has right child only
            node = node.right
        elif node.left and not node.right: # node has left child only
            node = node.left
        else:
            pass
            node = self._pred_remove(node)
        return node

    def __ensure_balance(self, node):
        # Using rotations
        # node.height = max(node.left.height, node.right.height) + 1
        pass

    def __dfs_print(self, pointer, out : str) -> str:
        if not pointer:
            return out
        out = self.__dfs_print(pointer.left, out)
        out += str(pointer.key) + ", "
        out = self.__dfs_print(pointer.right, out)
        return out

    def print(self):
        print(self.__dfs_print(self.root, "[") + "]")                    

if __name__ == "__main__":
    tree = Tree()
    tree.insert(8)
    tree.insert(1)
    tree.insert(27)
    tree.insert(2)
    tree.insert(4)
    tree.insert(4)
    tree.print()
    print(tree.root.height)