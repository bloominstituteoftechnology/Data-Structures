class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    test = BinarySearchTree(value)
    if value > self.value:
      if self.right is None:
        self.right = test
      else: 
        self.right.insert(value)
    else: 
      if self.left is None:
        self.left = test
      else: 
        self.left.insert(value)


  def contains(self, target):
    if target == self.value:
      return True
    elif target > self.value:
      if self.right:
        if self.right.value == target:
          return True
        else:
          self.right.contains(target)
      else:
        return False
    else: 
      if self.left:
        if self.left.value == target:
          return True
        else:
          self.left.contains(target)
      else:
        return False

  def get_max(self):
    max = self.value
    if self.right:
      max = self.right.get_max()
    return max

