class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    #check if the value being inserted is less than current value (left)
    if value < self.value:
      #check if the left child node has spot, if it does not place a new tree
      if not self.left:
        self.left = BinarySearchTree(value)
      #if it does, rerun the function for the next spot
      else:
        self.left.insert(value)
    #check if value being inserted is greater than current value (right)
    elif value >= self.value:
      #check if the right child node has spot open
      if not self.right:
        self.right = BinarySearchTree(value)
        #repeat process if spot is not empty
      else:
        self.right.insert(value)

    

  def contains(self, target):
    #checks if target is less than value then repeat check
    # checks if target is greater than value then repeat check
    # checks if target equal to value
    # if no value == target return false

    if self.value == target:
      return True
    elif self.value > target:
      if self.left == None:
        return False
      return self.left.contains(target)
    elif self.value < target:
      if self.right == None:
         return False
      return self.right.contains(target)

    

  def get_max(self):
    pass

  def for_each(self, cb):
    pass