class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    current = self
    while True:
      if current is None:
        return False
      if target == current.value:
        return True
      if target > current.value:
        current = current.right
      else:
        current = current.left

  def get_max(self):
    while True:
      if current.right is None:
        return current.value
      current = current.right

  def for_each(self, cb):
    pass