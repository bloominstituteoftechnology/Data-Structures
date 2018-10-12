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
    current = self
    while current:
      if target == current.value:
        return True
      elif target < current.value:
        current = current.left
      else:
        current = current.right
    return False

  def get_max(self):
    # returns the maximum value in the binary search tree
    current = self
    while current.right:
      current = current.right
    return current.value
    # value to the right is always meant to be the higher value, so while it exists, it's the maximum value; if it's not, then we get the current value
