class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value is None:
      self.value = value
    else:
      if value >= self.value:
        if not self.right:
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)
      else:
        if not self.left:
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)

  def contains(self, target):
    current = self
    contained = False
    while (current and not contained):
      if target > current.value:
        current = current.right
      elif target < current.value:
        current = current.left
      else:
        contained = True
    return contained

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value
