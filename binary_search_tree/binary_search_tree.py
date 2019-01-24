class BinarySearchTree:
  # log based 2
  # ternary tree would be log based 3
  def __init__(self, value):
    self.value = value
    self.left = None #left side smaller than root
    self.right = None#right side larger than root

  def insert(self, value): #O(logn) # you divide the searches of where to add it by 2
    tree = BinarySearchTree(value)
    # if value of the new tree is less then tree
    if value < self.value:
      if self.left is None:
        self.left = tree
      else: 
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = tree
      else:
        self.right.insert(value)

  def contains(self, target): #walk down till you find item or empty branch it doesn't exist
    current = self
    while True:
      if current is None:
        return False
      if target == current.value:
        return True
      if target > current.value: 
        current = current.right
      else:
        current = current.left

  def get_max(self): #all the way down right side till the end
    current = self
    while True:
      # when you reach the end then you'll be at the biggest value
      if current.right is None:
        return current.value # return max
      # keep incrementing on right side till the end
      current = current.right
    


# middle most value as root of the root