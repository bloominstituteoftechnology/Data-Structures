class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    node = BinarySearchTree(value)
    if self.value:
      if value > self.value:
        if self.right == None:
          self.right = value
        else:
          self.right.insert(value)
      if value < self.value:
        if self.left == None:
          self.left = value
        else:
          node.insert(value)
    else:
      self.value = value

  def contains(self, target):
    if target > self.value:
      if self.right == None:
        return False
      else: 
        return self.right.contains(target)
    elif target < self.value:
      if self.left == None:
        return False
      else:
        return self.left.contains(target)
    else:
      return True 

  def get_max(self):
    pass
  def for_each(self, cb):
    pass