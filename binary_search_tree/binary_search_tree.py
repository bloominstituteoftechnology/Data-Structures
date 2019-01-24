class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if not self.left and self.value > value:
      self.left = BinarySearchTree(value)
      return
    if not self.right and self.value < value:
      self.right = BinarySearchTree(value)
      return
    branch = self.left if self.value > value else self.right
    branch.insert(value)


  def contains(self, target):
    pass

  def get_max(self):
    pass
