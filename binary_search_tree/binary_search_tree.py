class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    newNode = BinarySearchTree(value)
    
    if self.value is None:
      self.value = value
      return
    
    if self.value <= value:
      if self.right is None:
        self.right = newNode
      else:
        self.right.insert(value)
    else:
      if self.left is None:
        self.left = newNode
      else:
        self.left.insert(value)
      

  def contains(self, target):
    if self.value == target:
      return True
    
    if self.value < target:
      if self.right is None:
        return False
        
      return self.right.contains(target)
      
    else:
      if self.left is None:
        return False
        
      return self.left.contains(target)

  def get_max(self):
    if self.right is not None:
      return self.right.get_max()
    
    return self.value
