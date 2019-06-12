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
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass