class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
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
    if self.value == target:
      return True
    elif target < self.value:
      if self.left is not None:
        return self.left.contains(target)
      else:
        return False
    elif target > self.value:
      if self.right is not None:
        return self.right.contains(target)
      else:
        return False

  def get_max(self):
    if self.right is not None:
      return self.right.get_max()
    else:
      return self.value

  def print_tree(self):
    if self.left is not None:
      self.left.print_tree()
    print(self.value)
    if self.right is not None:
      self.right.print_tree()

print('binary search tree ran')

# bst = BinarySearchTree(5)
# bst.insert(6)
# print(bst.contains(5))
# print(bst.contains(6))
# print(bst.contains(7))
# bst.insert(7)
# print(bst.contains(7))
# print(bst.get_max())
# bst.print_tree()

