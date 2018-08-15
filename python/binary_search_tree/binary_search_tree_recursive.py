# Title  : BST using recursive approach
# Author : Frank Faustino
# Date   : 2018-08-15

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target is self.value:
      return True

    if self.left and target < self.value:
      return self.left.contains(target)
    elif self.right and target > self.value:
      return self.right.contains(target)

    return False

  def get_max(self):
    max = self.value
    if self.right and max < self.right.value:
      return self.right.get_max()

    return max
