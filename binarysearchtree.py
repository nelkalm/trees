class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    """
    Removing a node...
    (1) If node is none --> return False
    (2) If node is not empty... 3 cases:
        2.1: Leaf node (no child)
        2.2: One child
        2.3: Two children
    """
    def remove(self, value):
        if self.root is not None:
            self.remove_node(value, self.root)
    
    def remove_node(self, value, target_node):
        if target_node is None:
            return
        # Step 1: Find the target node
        if value < target_node.value:
            self.remove_node(value, target_node.left)
        elif value > target_node.value:
            self.remove_node(value, target_node.right)
        else:

            # Step 2: Remove implementation if target node if found
            # Case 1: Removing a leaf node
            if target_node.left is None and target_node.right is None:
                parent = target_node.parent
                if parent is not None and parent.left == target_node:
                    parent.left = None
                if parent is not None and parent.right == target_node:
                    parent.right = None
                if parent is None:
                    self.root = None
                del target_node

            # Case 2: Removing a node with one child
            elif target_node.left is None and target_node.right is not None:
                parent = target_node.parent
                if parent is not None and parent.left == target_node:
                    parent.left = target_node.right
                if parent is not None and parent.right == target_node:
                    parent.right = target_node.right
                if parent is None:
                    self.root = parent.right
                target_node.right.parent = parent
                del target_node
            
            elif target_node.left is not None and target_node.right is None:
                parent = target_node.parent
                if parent is not None and parent.left == target_node:
                    parent.left = target_node.left
                if parent is not None and parent.right == target_node:
                    parent.right = target_node.left
                if parent is None:
                    self.root = parent.right
                target_node.left.parent = parent
                del target_node

            # Case 3: Removing a node with two children
            else:
                predecessor = self.get_predecessor(target_node.left)
                temp = predecessor.value
                predecessor.value = target_node.value
                target_node.value = temp
                self.remove_node(value, predecessor)


    def get_predecessor(self, target_node):
        if target_node.right is not None:
            return self.get_predecessor(target_node)
        return target_node

    def contain(self, value):
        # if self.root is None:
        #     return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

print(my_tree.contain(3))
print(my_tree.contain(6))

print(my_tree.min_value_node(my_tree.root).value)
print(my_tree.min_value_node(my_tree.root.right).value)

my_tree.remove(52)
print(my_tree.contain(52))
