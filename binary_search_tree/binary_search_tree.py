class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    if new_node.value >= self.value:
      if not self.right:
        self.right = new_node
      else:
        self.right.insert(value)
    else:
      if not self.left:
        self.left = new_node
      else:
        self.left.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    elif target >= self.value:
      if not self.right:
        return False
      else:
        return self.right.contains(target)
    else:
      if not self.left:
        return False
      else:
        return self.left.contains(target)

  def get_max(self):
    while self.right != None:
      self = self.right
    return self.value
    
    


tree = BinarySearchTree(8)
tree.insert(10)
print(tree.value)
print(tree.right.value)
print("Tree contains 8: ", tree.contains(8))
print("Tree contains 10: ", tree.contains(10))
print("Tree contains 33: ", tree.contains(33))

