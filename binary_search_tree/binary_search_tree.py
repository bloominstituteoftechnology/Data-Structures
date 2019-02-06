class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):  # O(log(n))
  
  # O(log(n)) because as the tree gets bigger, the depth of the tree, meaning the number of recursions, (depth) is always much less than the total number of items. The depth doesn't increase at the same rate as the number of items.
    
    # If the number already exists, skip it
    if value == self.value:  # O(1)
      return
      
    if value < self.value:  # O(1)
      if self.left is None:  # O(1)
        # making a new tree with the value with left and right being none
        self.left = BinarySearchTree(value)  # O(1)
      else: # left is not none
        self.left.insert(value)  
    elif self.value < value:  # O(1)
      if self.right is None:  # O(1)
        self.right = BinarySearchTree(value)  # O(1)
      else:
        self.right.insert(value)
        
  def contains(self, target): # O(log(n))
    
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

  def get_max(self):  # O(log(n))
    
    # The max is always on the right side. We can check is the current node has a right child, if it doesn't then it is the max value.
    
    if self.right is None:
      return self.value
    
    return self.right.get_max()
    
    
    # all the methods are O(log(n)) because we're comparing at the same depth.