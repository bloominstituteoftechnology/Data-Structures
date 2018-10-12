class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    tree = BinarySearchTree(value)
    if value < self.value:
      if not self.left:
        self.left = tree
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    if target < self.value:
      if self.left:
        if self.left.contains(target):
          return True
    else:
      if self.right:
        if self.right.contains(target):
          return True
    return False

  def get_max(self):
    if not self:
      return None
    if not self.right:
      return self.value
    return self.right.get_max()


