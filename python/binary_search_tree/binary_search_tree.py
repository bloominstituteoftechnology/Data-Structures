# Title  : BST using iterative approach
# Author : Frank Faustino
# Date   : 2018-08-15

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    node = BinarySearchTree(value)
    done = False

    while done is not True:
      if value < self.value:
        if not self.left:
          self.left = node
          done = True
        else:
          self = self.left
      else:
        if not self.right:
          self.right = node
          done = True
        else:
          self = self.right

  def contains(self, target):
    while self:
      if target is self.value:
        return True
      elif target < self.value:
        self = self.left
      else:
        self = self.right

    return False

  def get_max(self):
    max = self.value

    while self:
      if max < self.value:
        max = self.value
      self = self.right

    return max
