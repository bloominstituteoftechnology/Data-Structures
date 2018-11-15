class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_subtree = BinarySearchTree(value)
    # if value is less than root go to left side
    if (value < self.value):
      # if left side is empty
      if not self.left:
        # value becomes root of new_subtree
        self.left = new_subtree
      else:
        # else, insert the value
        self.left.insert(value)
    # if value is greater than or equal to root go to right side
    elif value >= self.value:
      # if right side is empty
      if not self.right:
        # value becomes root on new_subtree
        self.right = new_subtree
      else:
        # else, insert the value
        self.right.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass
