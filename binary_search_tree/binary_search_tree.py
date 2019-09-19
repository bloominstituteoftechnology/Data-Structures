import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value is None:
      self.value = value
    else:
      if self.value > value:
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
    if self.value == target:
      return self.value
    elif self.value < target:
      if self.left is None:
        return None
      return self.left.contains(target)
    else:
      if self.right is None:
        return None
      return self.right.contains(target)

  def get_max(self):
    pass

  def for_each(self, cb):
    pass
