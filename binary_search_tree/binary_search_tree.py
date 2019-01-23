class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == None:
      self.value = BinarySearchTree(value)
    elif value > self.value:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    elif value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

  def contains(self, target):
    if target < self.value:
      if self.left is None:
        return False
      else:
        self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        return False
      else:
        return self.right.contains(target)
    elif target == self.value:
      return True

  def get_max(self):
    while self.right is not None:
      self = self.right
    return self.value
