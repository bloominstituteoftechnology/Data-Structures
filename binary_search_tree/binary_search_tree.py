class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value == self.value:
        return
    elif value < self.value:
        if self.left == None:
            self.left = BinarySearchTree(value)
        else:
            self.left.insert(value)
    else:
        if self.right == None:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)

  def contains(self, target):
    if target == self.value:
        return True
    elif target < self.value:
        if self.left:
            return self.left.contains(target)
        else:
            return False
    else:
        if self.right:
            return self.right.contains(target)
        else:
            return False

  def get_max(self):
    if self.right == None:
      return self.value

    return self.right.get_max()
