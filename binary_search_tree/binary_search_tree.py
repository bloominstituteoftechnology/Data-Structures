class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  def __str__(self):
    return str(f'topnode: {self.value}, self.left: {self.left}, self.right: {self.right}')

  def insert(self, value):

    #after first time set up
    if self.left == None and self.right == None:
      if self.value > value:
        self.left = BinarySearchTree(value)
      elif self.value < value:
        self.right = BinarySearchTree(value)

    #add to the left after start
    if self.left != None and self.right == None and value < self.value:
      if value < self.left.value:
        self.left.left = BinarySearchTree(value)
      else:
        self.left.right = BinarySearchTree(value)


    #add to the right after start
    if self.left != None and self.right == None and value > self.value:
      self.right = BinarySearchTree(value)

    if self.left != None and self.right != None and value > self.value:
      if value > self.right.value:
        self.right.right = BinarySearchTree(value)
      else:
        self.right.left = BinarySearchTree(value)

    if self.left == None and self.right != None and value > self.value:
      if value > self.right.value:
        self.right.right = BinarySearchTree(value)
      else:
        self.right.left = BinarySearchTree(value)


  def contains(self, target):

    if self.value == target:
      return True

    if self.left.value == target:
      return True

    if self.right.value == target:
      return True

    if self.left.right.value == target:
      return True

    return False


  def get_max(self):
    biggest = self.value
    
    if self.right != None and self.left == None:
      biggest = self.right.value
      if self.right.right != None:
        biggest = self.right.right.value
    return biggest
