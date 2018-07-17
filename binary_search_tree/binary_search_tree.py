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
              
  def contains(self, value):
      if value < self.value:
            if self.left is None:
                  return None
            return self.left.contains(value)
      elif value > self.value:
            if self.right is None:
                  return None
            return self.right.contains(value)
      else:
            return self

  def get_max(self):
    if self.right:
          x = self.right
    else:
          return self.value
    max = self.value
    while True:
          if x.value > max:
                max = x.value
          if x.right is None:
                return max
          else:
                x = x.right
          

