class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value and not self.left:
      self.left = BinarySearchTree(value)
      return self.left
    elif value >= self.value and not self.right:
      self.right = BinarySearchTree(value)
      return self.right
    
    if value < self.value:
      self.left.insert(value)
    else:
      self.right.insert(value)


  def contains(self, target):
    if target == self.value:
      return True
    
    if target < self.value:
      node_val = self.left
    else:
      node_val = self.right
    
    if not node_val:
      return False
    
    return node_val.contains(target)

  def get_max(self):
    if not self.right:
      right = self.value
    else:
      right = self.right.get_max()
    
    return max(self.value, right)