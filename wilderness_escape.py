# Welcome to Wilderness Escape, an online Choose-Your-Own-Adventure.
# Our users get a unique story experience by picking the next chapter
# of their adventure.

print('Once upon a time…')


class TreeNode:

    def __init__(self, story_piece) -> None:
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while len(story_node.choices) != 0:
            choice = int(input('Enter 1 or 2 to continue the story: '))
            if choice not in [1, 2]:
                print('Choice is invalid.')
            else:
                chosen_index = choice - 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child


# VARIABLES
story_root = TreeNode(
    """
    You are in a forest clearing. There is a path to the left.
    A bear emerges from the trees and roars!
    Do you: 
    1 ) Roar back!
    2 ) Run to the left...
    """
)

choice_a = TreeNode(
    """
    The bear is startled and runs away.
    Do you:
    1 ) Shout 'Sorry bear!'
    2 ) Yell 'Hooray!'
    """
)

choice_b = TreeNode(
    """
    You come across a clearing full of flowers. 
    The bear follows you and asks 'what gives?'
    Do you:
    1 ) Gasp 'A talking bear!'
    2 ) Explain that the bear scared you.
    """
)

choice_a1 = TreeNode(
    """
    The bear returns and tells you it's been a rough week. After making peace with
    a talking bear, he shows you the way out of the forest.
    
    YOU HAVE ESCAPED THE WILDERNESS.
    """
)

choice_a2 = TreeNode(
    """
    The bear returns and tells you that bullying is not okay before leaving you alone
    in the wilderness.
    
    YOU REMAIN LOST.
    """
)

choice_b1 = TreeNode(
    """
    The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
    
    YOU REMAIN LOST.
    """
)

choice_b2 = TreeNode(
    """
    The bear understands and apologizes for startling you. Your new friend shows you a 
    path leading out of the forest.
    
    YOU HAVE ESCAPED THE WILDERNESS.
    """
)

user_choice = input('What is your name? ')
print(user_choice)

# TESTING
# print(story_root.story_piece)
story_root.add_child(choice_a)
story_root.add_child(choice_b)
story_root.traverse()
choice_a.add_child(choice_a1)
choice_a.add_child(choice_a2)
choice_b.add_child(choice_b1)
choice_b.add_child(choice_b2)
