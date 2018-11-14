class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == None:
      self.value = value
      return
    elif value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
        return
      else:
        self.left.insert(value)
    elif value > self.value:
      if self.right == None:
        self.right = BinarySearchTree(value)
        return
      else:
        self.right.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    
