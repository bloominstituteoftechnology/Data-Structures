"""
BST is node-based
Left subtree contains only keys(values) less than node's key
Right subtree contains only keys(values) greater than node's key
"""

"""
Create Node class with 3 attributes:
left
right
node data (it looks like you all are using "value" instead of "data"
It looks like this is already done for me!
"""

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

"""
Need insert method to create nodes
param value is data object to insert
"""

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
"""
First, compare the value passed in with the node - > or <?
If <, check the left node. If nothing is there, congratulations, you have a new left node!
If something is there, insert the new value.
Same with the right. If nothing is there, then you have a new right node.
If something is there, insert the new value.
"""

"""
Need method to look for specific nodes in the tree
param target is data object (value) we will compare with nodes
looking for a match
"""

  def contains(self, target):

"""
I guess get_max means we're supposed to return the largest value in the tree???
Maybe use stack to traverse the tree
"""

  def get_max(self):
    pass
