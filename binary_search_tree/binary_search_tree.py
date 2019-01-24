class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value): #insert includes getmax
    #if left branch is empty and value is less than root node (self.value)
    #set new instance with that value to the left.
    if self.left is None and value < self.value:
      self.left = BinarySearchTree(value)
      return 
    # if right empty and value bigger: vice versa
    if self.right is None and value > self.value:
      self.right = BinarySearchTree(value)
      return 
    #set new node to left if lesser else to right
    if value < self.value:
      new_node = self.left
    else: 
      self.right
    new_node.insert(value)
#what about = to??

  def contains(self, target):
    #first compare target to root
    if self.value is None or self.value == target:
      return self.value 
    #if root is less than target search right
    elif self.value < target: 
      return search(self.right, target)
    #if root is greater than target
    else:
      return search(self.left, target)

  def get_max(self): 
    #loop through right side to find leaf with largest value
    if self.value is None:
      return None
    while self.right:
      return self.right.get_max()
    else:
      return self.value

  
  