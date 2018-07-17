"""
BST is node-based
Left subtree contains only values less than node's value
Right subtree contains only values greater than node's value
"""

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# param value is the data object to insert
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

# First, compare value passed in with the node - > or <?
# If <, check left node. If nothing is there, congratulations - you have a new node.
# If something is there, insert the new value
# Same with the right.
# Ignore new value if equal to current node value

    def contains(self, target):
        if target == self.value:
            return self
        if target < self.value:
            if self.left is None:
                print('doh!')
            else:
                return self.find(target, node.left)
        elif target > self.value:
            if self.right is None:
                print('doh!')
            else:
                return self.find(target, node.right)
        else:
            print(int(self.value) + 'is present')
# This is similar to above where we compare the target with the node value and then look down each subtree

    def get_max(self):
        if self is none or self.left is None:
            return self
        current = self
        while current:
            if not current.right:
                return current
            current = current.right
