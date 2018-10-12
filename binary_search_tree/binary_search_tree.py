class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # wrap the value in a new tree node
    new_tree = BinarySearchTree(value)
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    # base case
    if self.value == target:
      return True
    elif target < self.value:
      if self.left:
        return self.left.contains(target)
      else:
        if self.right:
          return self.right.contains(target)
      return False

  def get_max(self):
    if not self:
      return None
