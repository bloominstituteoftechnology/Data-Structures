class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value > self.value:
      if self.right is None:
        self.right = [value]
      else:
        self.right.append(value)
    elif value < self.value:
      if self.left is None:
        self.left = [value]
      else:
        self.left.append(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target > self.value:
      for value in self.right:
        if value == target:
          return True
      return False
    elif target < self.value:
      for value in self.left:
        if value == target:
          return True
      return False
    else: return False

  def get_max(self):
    if self.right is None:
      return self.value
    else:
      self.right.sort()
      return self.right[len(self.right)-1]
