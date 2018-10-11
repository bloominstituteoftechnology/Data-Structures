class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    bst = BinarySearchTree(value)
    if bst.value < self.value:
        if not self.left:
            self.left = bst
        else:
            self.left.insert(value)
    if bst.value >= self.value:
        if not self.right:
            self.right = bst
        else:
            self.right.insert(value)

  def contains(self, target):
    if target == self.value:
        return True
    elif target < self.value:
        if self.left:
            return self.left.contains(target)
    elif target >= self.value:
        if self.right:
            return self.right.contains(target)

    return False

  def get_max(self):
    if self.right:
        return self.right.get_max()
    return self.value
