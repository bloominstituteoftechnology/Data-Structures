class BinarySearchTree:
  def __init__(self, value):
    # the value at the current node
    self.value = value
    # reference to this node's left child
    self.left = None
    # reference to this node's right child
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
    # check if the node's value is equal to our node's current value
    if target == self.value:
      # if it is return true
      return True
    elif self.right is None and self.left is None:
      return False
    else:
      if self.left is not None:
        if self.left.contains(target):
          return True
      if self.right is not None:
        if self.right.contains(target):
          return True

  def get_max(self):
    if self.right is None:
      return self.value
    else:
      return self.right.get_max()

  def for_each(self, cb):
    
    # check if the node's value is equal to our node's current value
    cb(self.value)
    if self.right is None and self.left is None:
      return
    else:
      if self.left is not None:
        self.left.for_each(cb)
      if self.right is not None:
        self.right.for_each(cb)
    
    return

		# it'd poorly weighted	