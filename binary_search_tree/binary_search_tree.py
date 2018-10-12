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
      return True
    elif target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    elif target > self.value:
      if not self.right:
        return False
      else:
        return self.right.contains(target)
    else:
      return False
       

  def get_max(self):
    if self.right == None:
      return self.value
    else:
      return self.right.get_max()
