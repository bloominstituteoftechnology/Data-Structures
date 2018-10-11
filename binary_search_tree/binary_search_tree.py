class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value >= self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    else:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    if target > self.value:
      if self.right is None:
        return False
      else:

  def get_max(self):
    pass
