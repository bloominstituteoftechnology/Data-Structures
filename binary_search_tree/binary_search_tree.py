class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.head = None

  def insert(self, value):
    #wrap the value in bst
    new_tree = BinarySearchTree(value)
    # see if new node < current node
    if value < self.value:
      if not self.left:
        self.left = new_tree
      else:
        #recursion
        self.left.insert(value)
    # value is >= to the cur val
    else: 
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)
    """if self.value:
      if value < self.value:
        if self.left is None:
          self.left = BinarySearchTree(value)
        else: self.left.insert(value)
      elif value > self.value:
        if self.right is None:
          self.right = BinarySearchTree(value)
        else: 
          self.right.insert(value)
    else:
      self.value = value
"""
  def contains(self, target):
    # if the val of cur matches tar, done
    if self.value == target:
      return True
    #if value < the cur node val, call contain on left subtree
    if target < self.value:
      #check if self.left exists
      if self.left:
        if self.left.contains(target):
          return True
    else:
      if self.right:
        if self.right.contains(target):
          return True
    return False
    """if target < self.value:
      if self.left is None:
        return None
      return self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        return None
      return self.right.contains(target)
    else:
      return self
    """
  def get_max(self):
    # no point in doing this if tree empty
    if not self:
      return None
    # Check to see if the right side exists
    if not self.right:
      return self.value
    # we still have more children
    return self.right.get_max()


