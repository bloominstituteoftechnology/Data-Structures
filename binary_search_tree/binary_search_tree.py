class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
        return
      else:
        self.left.insert(value)

    if value > self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
        return
      else:
        self.right.insert(value)

  def contains(self, target):
    if target < self.value and self.left is not None:
      if self.left.value == target:
        return True
      else:
        self.left.contains(target)
    if target > self.value and self.right is not None:
      if self.right.value == target:
        return True
      else:
        self.right.contains(target)

    return False

  def get_max(self):
    max_value = self.value

    if self.right is None:
      return max_value
    else:
      return self.right.get_max()
