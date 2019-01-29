class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value > self.value:
      self.right = value
    elif value < self.value:
      self.left = value
      

  def contains(self, target):
    pass

  def get_max(self):
    pass
