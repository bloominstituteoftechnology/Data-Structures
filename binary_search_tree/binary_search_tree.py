class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value is None:
      self.value = value;
    else:
      if value < self.value:
        if self.left is None:
          self.left = BinarySearchTree(value)
        else:
          # check next node recursively
          self.left.insert(value)

      elif value > self.value:
        if self.right is None:
          self.right = BinarySearchTree(value)
        else: 
          self.right.insert(value)

  def contains(self, target):
    if self is None:
      return False
    else: 
      if self.value is target:
        return True
      else:
        if target < self.value and self.left is not None:
          return self.left.contains(target)
        elif target > self.value and self.right is not None:
          return self.right.contains(target)
        else: 
          return False

  def get_max(self):
    # max will always be farthest right node
    if self.right is None: 
      return self.value
    else: 
      return self.right.get_max()

