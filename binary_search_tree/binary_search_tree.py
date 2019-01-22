class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:                        # if the value is less than the current node
      if self.left == None:                       # if the current node doesnt have a left child
        self.left = BinarySearchTree(value)       # create a new node and set the child of the current node equal to that new node. that new node is going to be storing the value that we want to insert
      else:
        self.left.insert(value)                   # if current node does have a left child, insert the current node left child as the current node
    else:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:                  # if current value is equal to target
      return True                             # return true
    elif target < self.value:                 # else if target is less than current value
      if self.left == None:                   # if the left side of the current value is empty
        return False                          # return false
      return self.left.contains(target)       # else return left side target value
    elif target > self.value:
      if self.right == None:
        return False
      return self.right.contains(target)
    else:                                     # else no target value found
      return False                            # return false

  def get_max(self):
    if self.right == None:
      return self.value
    else:
      return self.right.get_max()
