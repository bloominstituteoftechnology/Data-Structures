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
    if target == self.value:
      return True
    branch = self.left if target < self.value else self.right
    if not branch:
      return False
    return branch.contains(target) 

  def get_max(self):
    if not self.right:
      return self.value
    return max(self.value, self.right.get_max())
