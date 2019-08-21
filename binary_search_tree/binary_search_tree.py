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
    pass

  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left:
        return self.left.contains(target)
        # self.left.value
        # return self.contains(target)
      else:
        return False
    elif target > self.value:
      if self.right:
        return self.right.contains(target)
        # self.value = self.right.value
        # return self.contains(target)
      else:
        return False
    pass

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else: 
      return self.value
    
    pass

  def for_each(self, cb):
    pass