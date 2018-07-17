class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value > self.value and self.right == None:
      self.right = BinarySearchTree(value)
      return
    elif value < self.value and self.left == None:
      self.left = BinarySearchTree(value)
      return
    
    if value < self.value:
      x = self.left
    if value > self.value:
      x = self.right

    while True:
      if value > x.value and x.right == None:
        x.right = BinarySearchTree(value)
        return
      elif value < x.value and x.left == None:
        x.left = BinarySearchTree(value)
        return
      else:
        if value < x.value:
          x = x.left
        if value > x.value:
          x = x.right

  def contains(self, target):
    current = self.value
    if target == current:
      return True
    elif target < current:
      if self.left:
        return self.left.contains(target)
      else:
        return False
    else:
      if self.right:
        return self.right.contains(target)
      else:
        return False

  def get_max(self):
    pass
