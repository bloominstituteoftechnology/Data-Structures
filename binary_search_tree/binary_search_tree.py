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
    if self.value == target:
      return False
    if self.value == target:
      return 
    elif self.value > target:
      if target == self.left.value:
        return 
    elif self.value < target:
      if target == self.right.value:
        return True

    return False
    

  def get_max(self):
    pass

  def for_each(self, cb):
    pass