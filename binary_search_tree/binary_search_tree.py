class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.left is None and value < self.value:
      self.left = BinarySearchTree(value)
      return

    if self.right is None and value > self.value:
      self.right = BinarySearchTree(value)
      return

    if value < self.value:
      branch = self.left
      branch.insert(value)
    else:
      branch = self.right
      branch.insert(value)
      
  def contains(self, target):
    pass

  def get_max(self):
    pass
