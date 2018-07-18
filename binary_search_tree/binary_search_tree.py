class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value is None:
      return None
    elif value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    
  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left is None:
        return False
      else: 
        return self.left.contains(target)
    else:
      if self.right is None:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    if not self:
      return None
    if not self.right:
       return self.value
    return self.right.get_max()
