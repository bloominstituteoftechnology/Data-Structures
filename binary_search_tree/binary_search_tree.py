class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value > value:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    if self.value <= value:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.value > target:
      if self.left == None:
        return False
      return self.left.contains(target)
    if self.value < target:
      if self.right == None:
        return False
      return self.right.contains(target)

  def get_max(self):
    if self.right == None:
      return self.value
    return self.right.get_max()

