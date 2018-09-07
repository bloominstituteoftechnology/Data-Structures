class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.root = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    if value < self.value:
      if not self.left:
        self.left = new_node
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = new_node
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if target < self.value:
      if self.left:
        if self.left.contains(target):
          return True
    else:
      if self.right:
        if self.right.contains(target):
          return True
    return False

  def get_max(self):
    max_val = self.value
    current = self
    while current:
      if current.value > max_val:
        max_val = current.value
      current = current.right
    return max_val
