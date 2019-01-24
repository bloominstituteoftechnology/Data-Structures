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
    elif value > self.value:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)


  def contains(self, target):
    if self.value == target:
      return True

    if self.value:
      if target < self.value:
        return self.left.contains(target) if self.left else False
      elif target > self.value:
        return self.right.contains(target) if self.right else False
    elif not self.value:
      return False

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value
