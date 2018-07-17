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
    if target == self.value:
      return True
    if target < self.value:
      if self.left == None:
        return False
      return self.left.contains(target)
    else:
      if self.right == None:
        return False
      return self.right.contains(target)

  def get_max(self):
    val_max = self.value
    right = self.right
    while right != None:
      val_max = right.value
      right = right.right
    return val_max
