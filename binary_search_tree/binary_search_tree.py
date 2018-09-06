class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # Recursive solution
    if self.value > value: # If the current value is >input value continue:
      if self.left == None: # If left branch is none ->
        self.left = BinarySearchTree(value) # -> Assign left branch to the value of the current binary tree
      else:
        self.left.insert(value)
    if self.value <= value:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

    #********* Iterative Solution **********
    # current_tree = self
    # placed = False
    # while not placed:
    #   # Passed in value is smaller than current_tree value
    #   if value < current_tree.value:
    #     if current_tree.left == None:   # Place it there if no node present
    #       current_tree.left = BinarySearchTree(value)
    #       placed = True
    #     else:
    #       current_tree = current_tree.left  # Or move one tree down
    #   # Passed in value is greater than (or equal to) current_tree value
    #   else:
    #     if current_tree.right == None:
    #       current_tree.right = BinarySearchTree(value)
    #       placed = True
    #     else:
    #       current_tree = current_tree.right

  def contains(self, target):
    # Recursive solution
    if self.value == target:
      return True
    if self.value > target: 
      if self.left == None:
        return False
      return self.left.contains(target)
    if self.value < target: 
      if self.right == None:
        return False
      return self.right.contains(target)

    # ********** Iterative Solution ***********
    # current_tree = self
    # while True:
    #   if current_tree == None:
    #     return False
    #   if current_tree.value == target:
    #     return True
    #   # Passed in value is smaller than current_tree value
    #   if target < current_tree.value:
    #     current_tree = current_tree.left 
    #   # Passed in value is greater than (or equal to) current_tree value
    #   else:
    #     current_tree = current_tree.right

  def get_max(self):
    # Recursive solution
    if self.right == None:
      return self.value
    return self.right.get_max()

    #********** Iterative Solution *********
    # current_tree = self
    # max_val = current_tree.value
    # while True:
    #   if current_tree.value > max_val:
    #     max_val = current_tree.value
    #   if current_tree.right == None:
    #     return max_val
    #   else:
    #     current_tree = current_tree.right
  
