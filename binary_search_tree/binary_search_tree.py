class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    node = BinarySearchTree(value)
    # if value is less than self.value
    if value < self.value:
    ## check if left is none
      if self.left == None:
        ## if so, set left to be this node
        self.left = node
      ## if not, call the left node's insert with this value
      else:
        self.left.insert(value)

    else:
      # if value is greater than or equal self.value
      if value >= self.value:
        # check if right is none 
        if self.right == None:
          ## if it is none, set right to be a node
          self.right = node
        ## if it has a node, call self.right.insert with this value
        else:
          self.right.insert(value)
  

  def contains(self, target):
    # if self.value is the target,
    if self.value == target:
      # return True
      return True

    # if the target is less than self.value,
    if target < self.value:
      # check if we have a left
      if self.left:
        # if so return left.contains on the target
        return self.left.contains(target)
      # if not return False
      else:
        return False
    else:
      # otherwise the target must be greater than self.value
      if target > self.value:
        ## check if we have a right
        if self.right:
          ## if so, return self.right.contains on the target
          return self.right.contains(target)
        ## if not, return False
        else:
          return False


  def get_max(self):
    ## if we have a right
    if self.right:
      ## return right's get max
      return self.right.get_max()
    ## otherwise, return self.value
    else:
      return self.value


  def for_each(self, cb):
    # call the callback on the self's value
    cb(self.value)

    # if self.right
    if self.right:
      ## call rightie's for_each with the cb
      self.right.for_each(cb)

    # if self.left
    if self.left:
      ## leftie's for_each with the cb
      self.left.for_each(cb)
