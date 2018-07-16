class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == None:
      self.value = value
    else:
      if self.value < value:
        if self.right.value == None:
          self.right.value = value
      else:
        self.right.insert(value)

      if self.left.value == None:
        self.left = value
      else:
        self.left.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass
