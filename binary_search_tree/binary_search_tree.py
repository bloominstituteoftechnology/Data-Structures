class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # //check if the new nodes value is less than
    #   a. Is there a child? If not insert new node
    #   b. repeat the process
    if value <= self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left == None:
        return False
      else:
        self.left.contains(target)
    elif target > self.right:
      if self.right == None:
        return False
      else:
        self.right.contains(target)
        
  def get_max(self):
    pass

  def for_each(self, cb):
    pass