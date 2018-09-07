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

  def contains(self, target):
   if self.value == target:
      return True
   if self.left:
      if self.left.contains(target):
        return True
   if self.right:
      if self.right.contains(target):
        return True
   return False

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value
