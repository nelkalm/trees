# Problems:
# (1) Insert items with the following keys (in the given order) into
# an initially empty binary search tree:
# 30 ,  40 ,  24 ,  58 ,  48 ,  26 ,  11 ,  13 .
# Draw the tree after any two insertions.

# (2) The height of a node v in a rooted tree T is defined as the
# number of edges on the longest simple downwards path from the node v
# to a leaf. Write an algorithm that calculates the height of all nodes
# in a binary tree and has running time O(n).


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        temp = self.root
        while True:
            if node.value < temp.value:
                if temp.left is None:
                    temp.left = node
                    return True
                else:
                    temp = temp.left
            elif node.value > temp.value:
                if temp.right is None:
                    temp.right = node
                    return True
                else:
                    temp = temp.right
            else:
                return False

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # def depth(self, node):
    #     depth = 0
    #     while node is not self.root:
    #         node = node.parent
    #         depth += 1
    #     return depth

    def find_smallest(self):
        """Find the tree and return the smallest node"""
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        return temp


my_tree = BinarySearchTree()
my_tree.insert(30)
my_tree.insert(40)
my_tree.insert(24)
my_tree.insert(58)


print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

print(f"The height of my_tree is: {my_tree.height(my_tree.root)}")
# print(f"The depth of my_tree is: {my_tree.depth(my_tree.find_smallest())}")
print(f"The smallest value of my_tree is: {my_tree.find_smallest().value}")
