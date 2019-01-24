class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == value:
      return
    elif self.value < value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else: self.right.insert(value)
    elif self.value > value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else: self.left.insert(value)


  def contains(self, target):
    current_value = self.value
    if current_value == target:
      return True
    elif current_value < target and self.right is not None:
      if self.right.value == target:
        return True
      else: self.right.contains(target)
    elif current_value < target and self.left is not None:
      if self.left.value == target:
        return True
      else: self.left.contains(target)
    return False

  def get_max(self):
    max_value = self.value
    if self.right is None:
      return max_value
    else:
      return self.right.get_max()
