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
    elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)


  def contains(self, target):
    if target == self.value:
      return True
    elif target > self.value:
      if self.right == None:
        return False
      else:
        return self.right.contains(target)
    else:
      if not self.left:
        return False 
      else:
        return self.left.contains(target)


  def get_max(self):
    if not self.right:
      return self.value
    else:
      return self.right.get_max()
