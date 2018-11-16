class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left != None:
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
    elif value > self.value:
      if self.right != None:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)

  def contains(self, target):
    # recursively check the tree values
    if target == self.value:
      return True

    if target < self.value:
      if self.left == None:
        return False
      return self.left.contains(target)

    if target > self.value:
      if self.right == None:
        return False
      return self.right.contains(target)

  def get_max(self):
    if self.right == None:
      return self.value

    return self.right.get_max()
