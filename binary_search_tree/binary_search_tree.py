class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # wrap the value in a new tree node
    if self.value == None:
      self.value = value
    elif value > self.value:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    elif value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if target > self.value:
      if self.right == None:
        return False
      else:
        return self.right.contains(target)
    elif target < self.value:
      if self.left == None:
        return False
      else:
        return self.left.contains(target)

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
