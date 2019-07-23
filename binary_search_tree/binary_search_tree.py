class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      if self.value < value:
          if self.right is None:
              self.right = BinarySearchTree(value)
          else:
              self.right.insert(value)
      elif self.value >= value:
          if self.left is None:
              self.left = BinarySearchTree(value)
          else:
            self.left.insert(value)

  def contains(self, target):
      if target == self.value:
          return True
      elif self.right and self.value < target:
          return self.right.contains(target)
      elif self.left and self.value > target:
          return self.left.contains(target)
      else:
          return False

  def get_max(self):
      if self.right != None:
          return self.right.get_max()
      else:
          return self.value

  def for_each(self, cb):
      cb(self.value)

      if self.left != None:
          self.left.for_each(cb)
    
      if self.right != None:
          self.right.for_each(cb)
