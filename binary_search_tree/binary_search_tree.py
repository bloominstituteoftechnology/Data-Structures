class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.left is None and value < self.value:
      self.left = BinarySearchTree(value)
      return

    if self.right is None and value >= self.value:
      self.right = BinarySearchTree(value)
      return

    side = self.left if value < self.value else self.right
    side.insert(value)

  def contains(self, target):
    if self.value == target:
      return True

    side = self.left if target < self.value else self.right
    if side is None:
      return False

    return side.contains(target)

  def get_max(self):
    right_side = self.value if self.right is None else self.right.get_max()
    return max(self.value, right_side)
