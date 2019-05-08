import random

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current = self
    while current.value != value:
      if value > current.value:
        if current.right is not None:
          current = current.right
        else:
          current.right = BinarySearchTree(value)
      elif value < current.value:
        if current.left is not None:
          current = current.left
        else:
          current.left = BinarySearchTree(value)

  def contains(self, target):
    current = self
    while current.value != target:
      if target > current.value:
        if current.right is not None:
          current = current.right
        else:
          return False
      else:
        if current.left is not None:
          current = current.left
        else:
          return False
    if current.value == target:
      return True

  def get_max(self):
    current = self
    while current.right is not None:
      current = current.right
    return current.value

  def for_each(self, cb, node="initial"):
    if node == "initial":
      node = self
    if node == None:
      return
    cb(node.value)
    self.for_each(cb, node.left)
    self.for_each(cb, node.right)



