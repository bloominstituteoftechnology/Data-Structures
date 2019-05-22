"""  
BST is initialized with a value.
Its left child and right child properties are both BinarySearchTrees
The value of the left child must be smaller than the value of the parent node.
The value of the right child must be >= the value of the parent node.
"""


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    """ insert adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree. 
    1. Check if the value is >= or < than the value of the current node.
    2a. If >=, check if we have a right child.
        - If there is no right child, set the new node to be the right child.
        - Otherwise recursively do insert on the right child.
    2b. If <, check if we have a left child.
        - If there is no left child, set the new node to be the left child.
        - Otherwise recursively do insert on the left child.
    """

    def insert(self, value):
        # check if the passed in value is less than self.value
        if value < self.value:
            # check if we have a left child
            if not self.left:
                # we've found the correct position for our new node
                self.left = BinarySearchTree(value)
            # we have a left child
            else:
                # recursively do insert on the left child
                self.left.insert(value)
        # our value is >= the current node's value
        else:
            # check if we have a right child
            if not self.right:
               # we've found the correct position for our new node
                self.right = BinarySearchTree(value)
            else:
                # recursively do insert on the right child
                self.right.insert(value)
    """ contains searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not """

    def contains(self, target):
        pass

    """ get_max returns the maximum value in the binary search tree. """

    def get_max(self):
        pass

    """ for_each performs a traversal of every node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work. """

    def for_each(self, cb):
        pass

    def __repr__(self):
        return f'{self.value}'


def traverse(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level


tree = BinarySearchTree(10)
tree.insert(11)
tree.insert(9)
tree.insert(12)
tree.insert(8)

traverse(tree)