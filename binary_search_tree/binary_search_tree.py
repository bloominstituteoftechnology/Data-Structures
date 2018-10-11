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
        return self.left.insert(value)
    elif value > self.value:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else: 
        return self.right.insert( value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target > self.value and self.right != None:
      return self.right.contains(target)
    elif target < self.value and self.left != None:
      return self.right.contains(target)
    else: 
      return False

  def get_max(self):
    if self.right == None:
      return self.value
    elif self.right and self.right.right == None:
      return self.right.value
    else:
      return self.right.get_max()
