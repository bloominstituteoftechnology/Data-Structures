class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value: # check if inputted valuw is less than the existing value
      if not self.left: # if there is no left node
        self.left = BinarySearchTree(value) # create a new node 
      else:
        self.left.insert(value) #insert the inputted value
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    elif target < self.value:
      if self.left:
        return self.left.contains(target) # check if the target value is on the left
    else:
      if self.right:
        return self.right.contains(target) # check if the target value is on the right

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.right
    return max_value


