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
    elif value >= self.value: 
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    else:
      if target < self.value and self.left is not None:
        if self.left.value == target:
          return True
        else:
          return self.left.contains(target)
      elif target > self.value and self.right is not None: 
        if self.right.value == target:
          return True
        else:
          return self.right.contains(target)
      return False
    
  def get_max(self):
    maxNode = self.value
    if self.right is None:
      return maxNode
    else:
      return self.right.get_max()
