class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # if value exists then return
    if value == self.value:
      return

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
    if target == self.value:
      return True

    if target < self.value:
      if self.left is None:
        return False
      else:
        return self.left.contains(target)

    if target > self.value:
      if self.right is None:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    if self.right is None:
      return self.value
    else:
      return self.right.get_max()
