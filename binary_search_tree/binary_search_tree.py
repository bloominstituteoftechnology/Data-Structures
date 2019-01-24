class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if not self.value:
      self.value = BinarySearchTree(value)
      return
    if self.value < value:
      if not self.right:
        self.right = BinarySearchTree(value)
        return
      else:
        self.right.insert(value)
        return
    else:
      if not self.left:
        self.left = BinarySearchTree(value)
        return
      else:
        self.left.insert(value)
    return

  def contains(self, target):
    if self.value == target:
      return True
    elif target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    pass
