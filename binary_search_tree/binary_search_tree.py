class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value): #insert includes getmax
    #if left branch is empty and value is less than root node (self.value)
    #set new instance with that value to the left.
    if value <= self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        return self.left.insert(value)
    # if right empty and value bigger: vice versa
    if value > self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        return self.right.insert(value)

  def contains(self, target):
    #first compare target to root
    if target == self.value:
      return True
    #if root is less than target search right
    if self.value < target:
      if self.right is None:
        return False
      else: 
        return self.right.contains(target)
    #if root is greater than target
    if self.value > target:
      if self.left is None:
        return False
      else:
        return self.left.contains(target)

  def get_max(self): 
    #loop through right side to find leaf with largest value
    if self.value is None:
      return None
    while self.right:
      return self.right.get_max()
    else:
      return self.value

  
  