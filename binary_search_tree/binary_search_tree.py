class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if value < self.value:
      if self.left is None:
        self.left = new_tree
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass
