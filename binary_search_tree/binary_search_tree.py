class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    tree = BinarySearchTree(value)
    if self.value > value:
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
    if self.value == target:
      return True
    
    if self.value > target:
      if self.left and self.left.contains(target):
        return True
    else:
      if self.right and self.right.contains(target):
        return True

  def get_max(self):
    if self.right:
      return self.right.get_max()
    return self.value

