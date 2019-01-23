class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
        return
      else:
       self = self.left
    elif value > self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
        return
      else:
        self = self.right
    else:
      pass
    self.insert(value)
    pass
    
    
  def contains(self, target):
    if target < self.value:
      if self.left is None:
        return False
      else:
        self = self.left
    elif target > self.value:
      if self.right is None:
        return False
      else:
        self = self.right
    elif target is self.value:
      return True
    return self.contains(target)
    

  def get_max(self):
    while self.right is not None:
      self = self.right
    return self.value
    pass
