class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

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
    pass
