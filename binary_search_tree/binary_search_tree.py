class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None # root of left_subtree
    self.right = None # root of right_subtree

  def insert(self, value):
    if value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
        # if no node exits, create new instance of BST
      else:
        self.left.insert(value) # else recursively call insert
    if value >= self.value:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left is not None:
        return self.left.contains(target)
      else:
        return False
    else: # target > self.value
      if self.right is not None:
        return self.right.contains(target)
      else:
        return False

  def get_max(self):
    max_value = self.value
    if self.right is None:
      return max_value
    else:
      return self.right.get_max()
