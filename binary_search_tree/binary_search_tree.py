class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


  def insert(self, value):   

    # if self.value:
    #   if value < self.value:
    #     if self.left is None:
    #       self.left = BinarySearchTree(value)
        
    #     else:
    #       self.left.insert(value)
      
    #   elif value > self.value:
    #     if self.right is None:
    #       self.right = BinarySearchTree(value)
    #     else:
    #       self.right.insert(value)
    
    # else:
    #   self.value = value

    #wrap the value in a BinarySearchTree instance
    new_tree = BinarySearchTree(value)
    #check and see if the new node's value is less than our current node's value
    if value < self.value:
      if not self.left:
        self.left = new_tree
      # there is a node there
      else:
        # repeat the whole process! 
        self.left.insert(value)
    # the value is >= to the current value
    else:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)


  def contains(self, target):    
    # checking if the value of the current node matches the target
    if target == self.value:
      return True
    # if value < the current node's value, call contains on the left subtree
    if target < self.value:
      #check if self.left exists 
      if self.left:
        if self.left.contains(target):
          return True
    
    else:
      if self.right:
        if self.right.contains(target):
          return True
    # if Tree doesn't contain target, return False
    return False


  # def get_max(self):
  #   max_value = self.value    

  #   while self.right is not None:
  #     max_value = self.right.value
  #   return max_value