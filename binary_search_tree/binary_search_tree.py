class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value > self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else: 
        insert(self,value)
    else: 
      if self.left is None:
        self.left = BinarySearchTree(value)
      else: 
        insert(self.left, value)


  def contains(self, target):
    pass

  def get_max(self):
    pass
