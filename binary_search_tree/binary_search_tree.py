class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value is None:
      self.value(value)
    pass

  def contains(self, target):
    pass

  def get_max(self, value):
    while value.right != None:
      value = value.right
    return value
    pass
