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
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left is None: return False
      else: return self.left.contains(target)
    else:
      if self.right is None: return False
      else: return self.right.contains(target)


  def get_max(self):
    max_value = self.value
    right = self.right
    while right is not None:
      max_value = right.value
      right = right.right
    return max_value
