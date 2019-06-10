class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    c = self
    while True:
      if value == self.value:
        break
      elif value < c.value:
        if not c.left:
          c.left = BinarySearchTree(value)
          break
        else:
          c = c.left
      else:
        if not c.right:
          c.right = BinarySearchTree(value)
          break
        else:
          c = c.right

  def contains(self, target):
    c = self
    while True:
      if c.value == target:
        return True
      elif target < c.value and c.left:
        c = c.left
      elif target > c.value and c.right:
        c = c.right
      else:
        return False

  def get_max(self):
    c = self
    while True:
      if c.right:
        c = c.right
      else:
        break
    return c.value

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)