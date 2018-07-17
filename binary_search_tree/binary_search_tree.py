class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
    else:
      if self.right == None:
        self.right = BinarySearchTree(value)
  

  def contains(self, target):
    if self.value == target:
      return True
    if self.value < target:
      if self.left == None:
        return False
      else:
        return self.left.contains(target)
    else:
      if self.right == None:
        return False
      else:
        return self.right.contains(target)
    pass

  def get_max(self, value):
    if not self:
      return None
    if not self.right:
      return self.value