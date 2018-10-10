class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    #"""if the value is greater than or equal to
    # insert it into the right side of the tree."""
    if value >= self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    else:
      #"""if the value is less than
    # insert it into the left side of the tree."""
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

  def contains(self, target):
    #""" if the target is equal to the self.value
    # return true. if not move on, target is greater than
    # value then access the right side then find if the right
    # side contains the value if so then end. If the value
    # is less than the self.value access the left side and
    # see if the left side contains the value. """
    if target == self.value:
      return True
    if target > self.value:
      if self.right is None:
        return False
      else:
        return self.right.contains(target)
    if target < self.value:
      if self.left is None:
        return False
      else:
        return self.left.contains(target)

  def get_max(self):
    #""" since the left side is filled with lower values 
    # just forget about it. go straight for the right side.
    # if the rigth side is None then just return the value
    # else find the max of value on the right side since
    # all the values on the right side are bigger than 
    # the core value of the tree."""
    if self.right is None:
      return self.value
    else:
      return self.right.get_max()


      # """    5
      #     4     6
      #    2 4   5 7   """
