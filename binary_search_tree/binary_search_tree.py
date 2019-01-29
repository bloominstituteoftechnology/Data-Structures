class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # if the left branch is empty and the value is less than self value 
    # set a new binary tree instance with value of value to the left branch then return to caller
    if self.left is None and value < self.value:
      self.left = BinarySearchTree(value)
      return
    # if the right branch is empty and the value is greater than or equal to self value 
    # set a new binary tree instance with value of value to the right branch then return to caller
    if self.right is None and value >= self.value:
      self.right = BinarySearchTree(value)
      return
    # set a new branch pointing to left if value is less than self value otherwise point it to the right
    branch = self.left if value < self.value else self.right
    # insert the value to the branch
    branch.insert(value)

  def contains(self, target):
    # if the target is the same as the self value return true
    if self.value == target:
      return True
    # set a new branch pointing to left if value is less than self value otherwise point it to the right
    branch = self.left if target < self.value else self.right
    # if the branch points nowhere return false to the caller
    if branch is None:
      return False
    # otherwise return a recursive call on target
    return branch.contains(target)

  def get_max(self):
    # set a right branch to the value if the right is empty otherwise set it to its own right.get max recursivly
    right_branch = self.value if self.right is None else self.right.get_max()

    # then return the max of the self value against the right branch
    return max(self.value, right_branch)
