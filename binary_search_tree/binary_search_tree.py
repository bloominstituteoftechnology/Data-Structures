class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # check if the new node's value is less than our current node's value
    if value < self.value:
      # if there's no left child here already, place the new node here
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        # otherwise, repeat the process!
        self.left.insert(value)
    # check if the new node's value is greater than or equal to our current node's value
    elif value >= self.value:
      # if there's no right child here already, place the new node here
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        # otherwise, repeat the process!
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
       return True

    if target < self.value :
      if not self.left:
        pass # do nothing because it is recursive loop
      else:
        if self.left.contains(target):
          return True

    elif target > self.value:
      if not self.right:
        pass
      else:
        if self.right.contains(target) :
          return True


  def get_max(self):
    if self.right :
      # return right most max value
      return self.right.get_max()
    else:
      # return root value
      return self.value
    

  def for_each(self, cb):
    cb(self.value)
    
    if self.left:
      self.left.for_each(cb)
    
    if self.right:
      self.right.for_each(cb)

    

    