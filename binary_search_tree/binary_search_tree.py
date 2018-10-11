class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value >= self.value:
        if self.right is None:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)
    else:
        if self.left is None:
            self.left = BinarySearchTree(value)
        else:
            self.left.insert(value)

  def contains(self, target):
    result = self.value
    if target == result:
        return True
    elif target > result and self.right is not None:
        if target == self.right.value:
            return True
        else:
            return self.right.contains(target)
    elif target < result and self.left is not None:
        if target == self.left.value:
            return True
        else:
            return self.left.contains(target)
    return False


  def get_max(self):
    maxx = self.value
    if self.right is None:
        return maxx
    else:
        return self.right.get_max()
