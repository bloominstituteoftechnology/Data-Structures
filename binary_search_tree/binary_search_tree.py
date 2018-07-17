"""
BST is node-based
Left subtree contains only keys(values) less than node's key
Right subtree contains only keys(values) greater than node's key
Create Node class with 3 attributes:
left
right
node data (it looks like you all are using "value" instead of "data"
"""

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#Insert method to create nodes
#param value is data object to insert
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

# First, compare the value passed in with the node - > or <?
# If <, check the left node. If nothing is there, congratulations, you have a new left node!
# If something is there, insert the new value.
# Same with the right. If nothing is there, then you have a new right node.
# If something is there, insert the new value.
# Ignore new value if equal to current one

# Contains: Method to look for specific nodes in the tree
# param target is data object (value) we will compare with nodes
# looking for a match

    def contains(self, target):
        if target == self.value:
            return self
        if target < self.value:
            if self.left is None:
                break
            else:
                return self.find(target, node.left)
        elif target > self.value:
            if self.right is None:
                break
            else:
                return self.find(target, node.right)
        else:
            print(int(self.value) + ' is present')
# This is similar to the above where we compare the target with the node value and then look down each subtree

# I guess get_max means we're supposed to return the largest value in the tree???

    def get_max(self):
        if self is none or self.left is None:
            return self
        current = self
        while current:
            if not current.right:
                return current
            current = current.right
