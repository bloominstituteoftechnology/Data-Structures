class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value:
      if value < self.value:
        # drop left
        if self.left is None:
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)
      elif value > self.value:
        # drop right
        if self.right is None:
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)
    else:
      self.value = value

  def contains(self, target):
    if target < self.value:
      if self.left is None:
        # Not Found
        return False
      return self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        # Not Found
        return False
      return self.right.contains(target)
    else:
      # Found
      return True

  def get_max(self):
      if self.right:
       return self.right.get_max()
    # else:
    #    return self.value
