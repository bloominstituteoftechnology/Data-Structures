class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        return self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        return self.right.insert(value)

  def contains(self, target):
    curr = self.value
    if curr == target:
      return True
    elif target < curr and self.left is not None:
      return self.left.contains(target)
    elif target > curr and self.right is not None: 
      return self.right.contains(target)
    return False


  def get_max(self):
    while self.right:
      return self.right.get_max()
    return self.value

