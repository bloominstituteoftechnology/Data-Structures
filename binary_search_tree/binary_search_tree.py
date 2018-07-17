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

    chosen = self.left if value < self.value else self.right
    chosen.insert(value)

  def contains(self, target):
    if self.value == target:
      return True

    chosen = self.left if target < self.value else self.right
    if chosen is None:
      return False

    return chosen.contains(target)

  def get_max(self):
    right = self.value if self.right is None else self.right.get_max()
    return max(self.value, right)