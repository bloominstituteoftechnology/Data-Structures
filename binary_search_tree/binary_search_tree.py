class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self == None:
      self = value
      return
    else:
      if self.value < value:
        if self.right == None:
          self.right = value
      else:
        insert(self.right, value)
    
      if self.left == None:
        self.left = value
      else:
        insert(self.left, value)

  def contains(self, target):
    pass

  def get_max(self):
    pass
