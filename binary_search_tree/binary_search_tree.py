class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_tree = BinarySearchTree(value) 
    if new_tree.value < self.value: 
      if self.left is None: 
        self.left = new_tree
      else:
        self.left.insert(new_tree.value) 
    elif new_tree.value > self.value: 
      if self.right is None: 
        self.right = new_tree
      else:
        self.right.insert(new_tree.value) 

  def contains(self, target):
    if self.value == target:
      return True
    elif target < self.value:
      if self.left is None:
        return False
      else: 
        return self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        return False
      else:
        return self.right.contains(target)
    else:
      return False

  def get_max(self):
    if self.right is None:
      return self.value
    else:
      return self.right.get_max()
