class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if not self.value:
      self.value = BinarySearchTree(value)
      return

    if self.value > value:
      if not self.left:
        self.left = BinarySearchTree(value)
        return
      self.left.insert(value)
      return

    if not self.right:
      self.right = BinarySearchTree(value)
      return
    self.right.insert(value)
    return

  def contains(self, target):
    if self.value == target:
      return True

    if self.value > target:
      if self.left == None:
        return False
      return self.left.contains(target)

    if self.right == None:
      return False
    return self.right.contains(target)

  def get_max(self):
    if self.right == None:
      return self.value
    return self.right.get_max()

