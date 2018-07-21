class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

    else: 
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)


  def contains(self, target):
    current = self.value
    if target == current:
      return True
    elif target > current:
      if self.right:
        return self.right.contains(target)
      else:
        return False
    else:
      if self.left:
        return self.left.contains(target)
      else:
        return False


  def get_max(self):
    if self.left and self.right is None:
      return None
    elif self.right:
      return self.right.get_max()
    else:
      return self.value

