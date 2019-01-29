class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):

    binary_tree = BinarySearchTree(value)
 
    #check if root is greater or equal than value
    if self.value < value:
      if self.right is None:
        self.right = binary_tree
      else:
        self.right.insert(value)
    else:
      if self.left is None:
        self.left = binary_tree
      else:
        self.left.insert(value)



    pass

  def contains(self, target):
    pass

  def get_max(self):
    pass
