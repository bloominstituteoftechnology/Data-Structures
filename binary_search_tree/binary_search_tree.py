

class BinarySearchTree:
  def __init__(self, value, parent=None):
    self.value = value
    self.left = None
    self.right = None
    self.parent = parent

  def insert(self, value):
    # need to check if there is a root, if there isn't set the first item as the root. 
    pass

  def contains(self, target):
    pass

  def get_max(self):
    current = self
    while current.hasRight():
      current = current.right
    return current
    
  def hasLeft(self):
    return self.left 
  
  def hasRight(self):
    return self.right
  
  def isLeft(self):
    return self.parent and self.parent.left == self 
  
  def isRight(self):
    return self.parent and self.parent.right == self 
  
  def isRoot(self):
    return not self.parent
  
  def isLeaf(self):
    return not (self.right or self.left)
  
  def has_a_child(self):
    return self.right or self.left 
  
  def has_max_children(self):
    return self.right and self.left 
  



  
  
