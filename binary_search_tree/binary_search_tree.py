class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_tree = BinarySearchTree(value)

    if value < self.value:
      if not self.left:
        self.left = new_tree
      else:
        #repeat the process
        self.left.insert(value)
    else:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    #check to see if value of current node matches the target
    if self.value == target:
      return True
  
      #if value < the current node value, call contains on the left subtree
    if target < self.value:
      #check if self.left exists
      if self.left:
        if self.left.contains(target):
          return True
    else:
      if self.right:
        if self.right.contains(target):
          return True
    
    #if we get here our tree doesn't contain target
    return False

  def get_max(self):
    #traverse the tree that has the greatest nodes(right side)
    # no point in doing anything if tree is empty
    if not self:
      return None
    #check to see if have a right side:
    if not self.right:
      return self.value
    return self.right.get_max()

