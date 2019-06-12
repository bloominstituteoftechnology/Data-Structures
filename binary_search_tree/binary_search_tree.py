class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value > self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    # test if the value is the target
    # if not the target, test if value is less than
    # run left value if it exists
    # if not less than, value is greater than
    # check right value if it exists
    if target == self.value:
      return True
    elif target > self.value and self.right != None:
        return self.right.contains(target)
    elif self.left != None:
        return self.left.contains(target)
    return False

  def get_max(self):
    # if no nodes, or if there is no right node, return the current value, as it is the maximum in the BST
    if self.value == None or self.right == None:
      return self.value
    # else, recursively call function, and run it until there is no right node
    return self.right.get_max()

    

  def for_each(self, cb):
    pass