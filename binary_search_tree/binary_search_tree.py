class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # wrap the value in a BinarySearthTree instance
    new_tree = BinarySearchTree(value)
    #check and see if the new node's value is less than our current node's value
    if value < self.value:
      # check to see if there is no left child here already, place the new node here
      if not self.left:
        self.left = new_tree
      #there is a node there
      else:
        # repeat the whole process with recursion
        self.left.insert(value)
    #the value is >= the current value
    else:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)
          

  def contains(self, target):
    #if the value of the current node matches the target, we're done
    if self.value == target:
      return True
      #if value < the current node's value, call contains on the left subtree
    if target < self.value:
      #check if self.left exists
      if self.left:
        if self.left.contains(target):
          return True
    else:
      if self.right:
        if self.right.contains(target):
          return True
    # our tree doesn't contain the target
    return False

  def get_max(self):
    #no point in doing anything if our tree is empty
    if not self:
      return None
    #check to see if we have a right side
    if not self.right:
      return self.value
    # otherwise we still have more children to the right
    return self.right.get_max()
