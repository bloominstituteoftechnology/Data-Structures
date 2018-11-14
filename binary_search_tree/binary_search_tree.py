class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      if value< self.value:
        if self.left is None:
          self.left = BinarySearchTree(value)
        else:
         self.left.insert(value)
      else:
        if self.right is None:
           self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)

    

  def contains(self, target):
    pass

  def get_max(self):
    # for a max value keep looking right
    if self.right:
      return self.right.get_max()
    return self.value

