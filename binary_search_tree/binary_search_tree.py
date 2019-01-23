class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if(self.value == None):
      self.value = BinarySearchTree(value)
    else:
      self._insert(value, self)
  def _insert(self, value, node):
    if(value < node.value):
      if(node.left != None):
        self._insert(value, node.left)
      else:
        node.left = BinarySearchTree(value)
    else:
      if(node.right != None):
        self._insert(value, node.right)
      else:
        node.right = BinarySearchTree(value)
        
    pass

  def contains(self, target):
    if target < self.value:
      if self.left is None:
        return False
      return self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        return False
      return self.right.contains(target)
    else:
      return self.value
    pass

  def get_max(self):
    current = self
    while current.right is not None:
      current = current.right
    return current.value

