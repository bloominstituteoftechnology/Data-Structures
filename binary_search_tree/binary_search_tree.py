class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # Add a node to the tree
  def insert(self, value):
    if self.value:
      
      if value < self.value:
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
    if self.value == target:
      return True
    elif target < self.value:
      branch = self.left
    elif target > self.value:
      branch = self.right
      if branch == None:
        return False
    return branch.contains(target)
    
  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value

test_bst = BinarySearchTree(1)
test_bst.insert(2)
test_bst.insert(3)
test_bst.insert(4)
test_bst.get_max()