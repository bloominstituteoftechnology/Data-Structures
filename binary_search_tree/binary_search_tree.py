class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.left is None and value < self.value:
      self.left = BinarySearchTree(value)
      return

    if self.right is None and value > self.value:
      self.right = BinarySearchTree(value)
      return

    if value < self.value:
      branch = self.left
      branch.insert(value)
    else:
      branch = self.right
      branch.insert(value)

  def contains(self, target):    
    branch = self.right if target > self.value else self.left

    if self.value == target: # --> Success case
      return True
    
    elif branch is None:
      return False
    
    return branch.contains(target)

  def get_max(self):
    # if self.right == None: # --> Check if there is any number than the base value at top of tree
    #   return self.value
    # else:
    #   return self.right.get_max() # --> Recursive call to check all right branch values

    # ------------ Better Way Using max() comparison method ----------------

    right_branch_value = self.value if self.right is None else self.right.get_max()

    return max(self.value, right_branch_value)
  
