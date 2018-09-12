class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    newNode = BinarySearchTree(value)
    if value > self.value:
      if self.right is not None:
        self.right.insert(value)
      else:
        self.right = newNode
    elif value < self.value:
      if self.left is not None:
        self.left.insert(value)
      else:
        self.left = newNode
    elif value == self.value:
      pass

  def contains(self, target):
    if target > self.value:
      if self.right is not None:
        return self.right.contains(target)
    if target < self.value:
      if self.left is not None:
        return self.left.contains(target)
    if target == self.value:
      return True

  def get_max(self):
    if self.right:
      return self.right.get_max()
    return self.value
