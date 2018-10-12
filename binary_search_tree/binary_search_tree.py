class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value <= self.value:
      if self.left:
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
    else:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left:
        return self.left.contains(target)
    elif target >= self.value:
      if self.right:
        return self.right.contains(target)

    return False

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