class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value > self.value:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    else:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif self.left==None and self.right==None:
      return False
    elif target > self.value:
      return self.right.contains(target)
    else:
      return self.left.contains(target)

  def get_max(self):
    if self.right==None:
      return self.value
    else:
      return self.right.get_max()
