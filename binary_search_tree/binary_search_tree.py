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
    # if self.value is None:
    #   self.value = value
    # else:
    #   if self.value < value:
    #     if self.right is None:
    #       self.right = value
    #     else:
    #       self.right.insert(value)
    #   else:
    #     if self.left is None:
    #       self.left = value
    #     else:
    #       self.left.insert(value)

    

  # def contains(self, target):
  #   if self.value is None or self.value == target:
  #     return self.value
    
  #   if self.value < target:
  #     return self.right.contains(target)

  #   return self.left.contains(target)

  # def get_max(self):
  #   pass 