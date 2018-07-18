class BinarySearchTree:
  def __init__(self, value):
    #initialize left and right value to None
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    #initialize new_tree as an instance of BinarySearchTree(value)
    new_tree = BinarySearchTree(value)
    #if value is less than self.value:
    if value < self.value:
      #if there's no left node, assert that self.left == new_tree
      if not self.left:
        self.left = new_tree
      else:
        #repeat the process
        self.left.insert(value)
    else:
      #if there's no right node value, assert that self.right == new_tree
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
        #if self.left exists, check to see if it contains the target
        if self.left.contains(target):
          return True
    else:
      if self.right: #if self.right exists, check to see if it contains the target
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

