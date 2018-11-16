class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value is None:
      self.value = value
    else:
      if self.value < value:
        if self.right:
          self.right.insert(value)
        else:
          # if self.right is None
          self.right = BinarySearchTree(value)
      else:
        if self.left:
          self.left.insert(value)
        else:
          # if self.right is None
          self.left = BinarySearchTree(value)


  def contains(self, target):
    if target is self.value:
      return True
    elif target < self.value and self.left:
      return self.left.contains(target)
    elif target > self.value and self.right:
      return self.right.contains(target)
    else:
      return False
    

  def get_max(self):
    if self.right == none:
      return self.value
    return self.right.get_max()