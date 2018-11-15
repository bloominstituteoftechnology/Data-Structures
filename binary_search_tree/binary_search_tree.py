class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == None:
      self.value = value
      return
    elif value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
        return
      else:
        self.left.insert(value)
        return
    elif value > self.value:
      if self.right == None:
        self.right = BinarySearchTree(value)
        return
      else:
        self.right.insert(value)
        return

  def contains(self, target):
    if self.value == None:
      return False
    elif self.value == target:
      return True
    elif target < self.value:
      if self.left != None:
        return self.left.contains(target)
    elif target > self.value:
      if self.right != None:
        return self.right.contains(target)


  def get_max(self):
    if self.right == None:
      return self.value
    else:
      return self.right.get_max()
