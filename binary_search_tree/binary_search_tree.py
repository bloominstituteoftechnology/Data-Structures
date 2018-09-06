class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    if value < self.value:
      if self.left is None:
        self.left = new_node
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = new_node
      else:
        self.right.insert(value)

  def contains(self, target):
    if target < self.value:
      if self.left is None:
        return False
      return self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        return False
      return self.right.contains(target)
    else:
      return True

  def get_max(self):
    pass
