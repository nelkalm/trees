class TreeNode:

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print('Adding ' + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print('Removing ' + child_node.value + ' from ' + self.value)
        # new_children = []
        # for item in self.children:
        #     if item is not child_node:
        #         new_children.append(item)
        # self.children = new_children
        self.children = [
            item for item in self.children if item is not child_node]

# Example 1
# root = TreeNode("I am Root")
# child = TreeNode("A wee sappling")
# bad_seed = TreeNode("Root Rot!")

# root.add_child(child)
# root.add_child(bad_seed)

# root.remove_child(bad_seed)

# Example 2
root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")

root.add_child(first_child)
root.add_child(second_child)


