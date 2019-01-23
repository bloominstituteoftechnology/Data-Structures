class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value <= self.value:
      if self.left is None:
        tree = BinarySearchTree(value)
        self.left = tree
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        tree = BinarySearchTree(value)
        self.right = tree
      else:
        self.right.insert(value)

      

  def contains(self, target):
    if target == self.value:
      return True

    if target <= self.value:
      if self.left is None:
        return False
      return self.left.contains(target)
    else:
      if self.right is None:
        return False
      return self.right.contains(target)
    

  def get_max(self):
    if self.value is None:
      return None
    
    if self.right is None:
      return self.value
    else:
      return self.right.get_max()
