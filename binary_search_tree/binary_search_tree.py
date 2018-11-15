class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value:
      if value < self.value:
        if self.left is None:
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)
      if value >= self.value:
        if self.right is None:
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)
    else:
      self.value = value

  def contains(self, target):
    if target == self.value:
      return True
    elif target > self.value:
      if self.right is None:
        return False
      elif target == self.right.value:
        return True
      else:
        self.right.contains(target)
    elif target < self.value:
      if self.left is None:
        return False
      elif target == self.left.value:
        return True
      else:
        self.left.contains(target)
    else:
      return False


  def get_max(self):
      if self.right is None:
        return self.value
      else:
        return self.right.get_max()
