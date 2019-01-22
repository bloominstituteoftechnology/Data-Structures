class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    tree =  BinarySearchTree(value)
    if self.value < value:
      if not self.right:
        self.right = tree
      else:
        self.right.insert(value)
    if self.value > value:
      if not self.left:
        self.left = tree
      else:
        self.left.insert(value)
      
  def contains(self, target):
    if target < self.value:
      if self.left is None:
        return False
      else:
        return self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        return False
      else:
        return self.right.contains(target)
    elif target == self.value:
      return True

  def get_max(self):
    if self.right is None:
      return self.value
    else:
      return self.right.get_max()


BinarySearchTree(7)
BinarySearchTree(7).contains(3)
