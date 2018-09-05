class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_Node = BinarySearchTree(value)
    if self.value == None:
      self.value = value
      return
    if self.value <= value:
      if self.right == None:
        self.right = new_Node
      else:
        self.right.insert(value)
    else:
      if self.left == None:
        self.left = new_Node
      else:
        self.left.insert(value)
  def contains(self, target):
    if self.value == target:
      return True
    if self.value < target:
      if self.right == None:
        return False
      return self.right.contains(target)
    else:
      if self.left == None:
        return False
      return self.left.contains(target)

  def get_max(self):
    if self.right != None:
      return self.right.get_max()
    return self.value
