class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if value < self.value:
      if self.left is None:
        self.left = new_tree
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):    
    if self.value == target:
      return True
    
    if target < self.value:
      if self.left is not None:
        return self.left.contains(target)
      else:
        return False

    if target > self.value:
      if self.right is not None:
        return self.right.contains(target)
      else:
        return False


  def get_max(self):
    pass
