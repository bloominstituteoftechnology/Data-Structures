class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # checking to see if value inserted is less than current value
    # and that there is no left value
    if value < self.value and not self.left:
      # sets left value to new value
      self.left = BinarySearchTree(value)
      # returns new set value
      return self.left
    # checks to see if value is greater than or equal to current value
    # and that there is no right value
    elif value >= self.value and not self.right:
      # sets right value to new value
      self.right = BinarySearchTree(value)
      # returns new set value
      return self.right
    
    # if there is a current value and it is greater than new value
    if value < self.value:
      # insert new value left
      self.left.insert(value)
    else:
      # else enter it right
      self.right.insert(value)


  def contains(self, target):
    # if target value is equal to current value
    if target == self.value:
      # return true
      return True
    # if target value is less than current value
    if target < self.value:
      # set node value to left value
      node_val = self.left
    else:
      # if target value is more than current value
      # set it to right value
      node_val = self.right
    
    if not node_val:
      return False
      
    return node_val.contains(target)

  def get_max(self):
    # if there is no right value
    if not self.right:
      # right equals current value
      right = self.value
    else:
      # if there is right value set right to right.get_max to run until max value found
      right = self.right.get_max()
    # return max value
    return max(self.value, right)