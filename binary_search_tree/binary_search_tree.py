class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # Value is less than current value
    if value < self.value:
      # if no left child, this is new left
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        # else add it to the left node
        self.left.insert(value)
    # value is equal to or greater than current value
    else:
      # if no right add to right 
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        # else add to right node
        self.right.insert(value)

  def contains(self, target):
    # finding data in tree
    current = self.value
    if target > self.left



  def get_max(self):
    pass
