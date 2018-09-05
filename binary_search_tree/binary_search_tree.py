class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value >= self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    # `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
    pass

  def get_max(self):
    # `get_max` returns the maximum value in the binary search tree.
    pass
