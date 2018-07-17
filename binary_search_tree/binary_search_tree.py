class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    #if value >= self.value:
     # if self.right == None:
      #  self.right = BinarySearchTree(value)
      #else:
        #self.right.insert(value)
    if value > self.value and self.right == None:
      self.right = BinarySearchTree(value)
      return
    elif value < self.value and self.left == None:
      self.left = BinarySearchTree(value)
      return
    if value < self.value:
      y = self.left
    if value > self.value:
      y = self.right

    while True:
      if value > y.value and y.right == None:
        y.right = BinarySearchTree(value)
        return
      elif value < y.value and y.left== None:
        y.left = BinarySearchTree(value)
        return
      else:
        if value < y.value:
          y = y.left
        if value > y.value:
          y = y.right


  def contains(self, target):
    if self.value != target and self.right == None and self.left == None:
      return False
    
    if target > self.value:
      y = self.right
    if target < self.value:
      y = self.left

    while True:
      if target == y.value:
        return True
      elif target > y.value and y.right == None:
        return False
      elif target < y.value and y.left == None:
        return False
      if target > y.value:
        y = y.right
      if target < y.value:
        y = y.left
      

  def get_max(self):
    if self.right:
      y = self.right
    else:
      return self.value
    max = self.value
    while True:
      if y.value > max:
        max = y.value
      if y.right == None:
        return max
      else:
        y = y.right
      