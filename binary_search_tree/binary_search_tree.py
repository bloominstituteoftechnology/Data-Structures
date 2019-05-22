"""
NST is initalize with a value.
Itss left child and right child properties are both BST
The value of the left child must be smaller that the value of the parent nonde.
The value of the left child must be equal or greater that the value of the parent nonde.
"""

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):

    # check if the passed in value is less than self.value
    if value < self.value:
      # check if we have left child
      if not self.left:
        # we've found the correct position for the new node
        self.left = BinarySearchTree(value)
        #we have a left child
      else:
        # recursively do insert on the lef child
        self.left.insert(value)
    else:
      # check if we have a right child:
      if not self.right:
        # we've found the correct position for the new node
        self.right = BinarySearchTree(value)
        #we have a left child
      else:
        # recursively do insert on the lef child
        self.right.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass

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
tree.insert(8)
tree.insert(12)