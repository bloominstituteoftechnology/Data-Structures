class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value > self.value and self.right is None:
      self.right = BinarySearchTree(value)
    if value < self.value and self.left is None:
      self.left = BinarySearchTree(value)
    if value > self.value:
      self.right.insert(value)
    if value < self.value:
      self.left.insert(value)
      

  def contains(self, target):
    if self.value is target:
      return True
    elif self.left is None and self.right is None:
      return False
    elif target > self.value:
      return self.right.contains(target)
    elif target < self.value:
      return self.left.contains(target)
    
    

  def get_max(self):
    maximum = 0
    if self.right is None:
      maximum = self.value
    while self.right is not None:
      maximum = self.value
      return self.right.get_max()
    return maximum
