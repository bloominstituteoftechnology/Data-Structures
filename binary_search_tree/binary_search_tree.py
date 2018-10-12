class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value is None:
      self.value = value
      return
    if value > self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
        return
      self.right.insert(value)
      return
    if self.left is None:
        self.left = BinarySearchTree(value)
        return
    self.left.insert(value)
    return
    

  def contains(self, target):
    if self.value == target:
      return True
    if  target > self.value and self.right is not None:
      return self.right.contains(target)
    if target < self.value and self.left is not None:
      return self.left.contains(target)
    return False
    

  def get_max(self):
    if self.right is not None:
      return self.right.get_max()
    return self.value
    
