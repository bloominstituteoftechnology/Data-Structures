class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_subtree = BinarySearchTree(value)
    # if value is less than root go to left side
    if (value < self.value):
      # if left side is empty
      if not self.left:
        # value becomes root of new_subtree
        self.left = new_subtree
      else:
        # else, insert the value
        self.left.insert(value)
    # if value is greater than or equal to root go to right side
    elif value >= self.value:
      # if right side is empty
      if not self.right:
        # value becomes root on new_subtree
        self.right = new_subtree
      else:
        # else, insert the value
        self.right.insert(value)

  def contains(self, target):
    # if root equals target
    if self.value == target:
      # return True
      return True
    # Look at the left side  
    if self.left:
      # if left side contains target
      if self.left.contains(target):
        # return True
        return True
    # Look at the right side    
    if self.right:
      # if right side conatins target
      if self.right.contains(target):
        # return True
        return True
    # otherwise, return False    
    return False


  def get_max(self):
    # if no root 
    if not self:
      # return None
      return None
    # declare that the max value equals the main root
    max_value = self.value
    # declare that current becomes the root node in question
    current = self
    while current:
      # if the current value in question is greater than the max value
      if current.value > max_value:
        # current.value becomes the max value
        max_value = current.value
      #  current becomes the child node on the right, because it’s greater
      current = current.right
    # return max value  
    return max_value
