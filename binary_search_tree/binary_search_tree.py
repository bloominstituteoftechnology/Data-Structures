class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    
    # If the number already exists, skip it
    if value == self.value:
      return
      
    if value < self.value:
      if self.left is None:
        # making a new tree with the value with left and right being none
        self.left = BinarySearchTree(value)
      else: # left is not none
        self.left.insert(value)
    elif self.value < value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
        
  def contains(self, target):
    
    if target == self.value:
      return True
      
    if target < self.value:
      if self.left is None:   # our target is not in there
        return False
      
      # If there is a left, check its children. Does the left contain the target?
      return self.left.contains(target)
      
    elif self.value < target:
      if self.right is None:
        return False
        
      return self.right.contains(target)

  def get_max(self):
    
    # The max is always on the right side. We can check is the current node has a right child, if it doesn't then it is the max value.
    
    if self.right is None:
      return self.value
    
    return self.right.get_max()