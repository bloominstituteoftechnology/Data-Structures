class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
    current = self
    parent = None
    while current:
      parent = current
      if value < current.value:
        current = current.left
      else:
        current = current.right
      # alternatively could be
      # elif value > current.value:
      #   current = current.right

  def contains(self, target):
    # searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not
    pass

  def get_max(self):
    # returns the maximum value in the binary search tree
    pass
