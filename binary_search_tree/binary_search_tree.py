class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    # The value at the top is the root node
    # The nodes with no children are leaf nodes
    self.left = None
    # Everything to the left of the binary tree,
    #  the child nodes must be smaller than the parent node
    self.right = None
    # Everything to the right of the binary tree,
    # the child nodes must be bigger than the parent node

  def insert(self, value):
    pass

  def contains(self, target):
    pass

  def get_max(self):
    pass
