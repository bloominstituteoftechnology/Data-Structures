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
    
    elif self.right == None and self.left == None:
      return False
    elif self.value > target:
        return self.left.contains(target)

    else:
       return self.right.contains(target)

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value
