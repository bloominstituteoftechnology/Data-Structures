class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # instatiate a new node in the search tree
    newNode = BinarySearchTree(value)

    # put the value on the right or left
    if value < self.value:
      # add the newNode as the left child if one doesn't exist
      if not self.left:
        self.left = newNode
      else: 
        # exist, so recurse
        self.left.insert(value)
    
    elif value >= self.value:
      # add the newNode as the right child if one doesn't exist
      if not self.right:
        # no right endpoint so add newNode
        self.right = newNode
      else:
        # exist, so recurse
        self.right.insert(value)

  def contains(self, target):
    if self.value == target: return True 
    
    if target < self.value:
      # check the left side 
      if self.left:
        #recurse
        if self.left.contains(target): return True 
    else: 
      # check the right side
      if self.right:
        # recurse
        if self.right.contains(target): return True 

    # target not found
    return False 


  def get_max(self):
    if not self: return None 

    max = self.value 
    current = self  

    while(current):
      if current.value > max: 
        max = current.value 

      current = current.right 
    
    return max 
