class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value:

      if value < self.value:
        if self.left is None:
            self.left = BinarySearchTree(value)
        else:
            self.left.insert(value)

      elif value > self.value:
        if self.right is None:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)

    else:
        self.value = value
    
  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left == None:
        return None
      else:
        return self.left.contains(target)
    else:
      if self.right == None:
        return None
      else:
        return self.right.contains(target)

  def get_max(self):
    max_num = self.value
    if self.right == None:
      return max_num
    elif self.right.value < max_num:
      return max_num
    else:
      return self.right.get_max()