class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):

    binary_tree = BinarySearchTree(value)
 
    #check if root is greater or equal than value
    if self.value < value:
      #value greater than root, place value to right side
      if self.right is None:
        self.right = binary_tree
      else:
        # repeat process of insert method until reach correct spot
        self.right.insert(value)
    else:
      if self.left is None:
        self.left = binary_tree
      else:
        self.left.insert(value)


  def contains(self, target):
    
    if target == self.value:
      return True
    # if target is less than root, traverse to left
    if target < self.value:
      if self.left:
        return self.left.contains(target)
    # else traverse right side
    else:
      if self.right:
        return self.right.contains(target)
    
  def get_max(self):
    # need to traverse down right side only
    # to get highest value
    if self.right:
      return self.right.get_max()
    else:
      return self.value
