class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    bst = BinarySearchTree(value)
    if value < self.value:
        if not self.left:
            self.left = bst
        else:
            self.left.insert(value)
    else: #case that inserted value is >= BST value
        if not self.right:
            self.right = bst
        else:
            self.right.insert(value)

  def contains(self, target):
    if self.value == target:
        return True
    elif target < self.value:
        if self.left and self.left.contains(target):
            return True
    else:
        if self.right and self.right.contains(target):
            return True
    return False


  def get_max(self):
    max_value = self.value
    if self.right:
        return self.right.get_max()

    return self.value
