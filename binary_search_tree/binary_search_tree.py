class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = self.right = None

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
    elif target > self.value:
      if self.right:
        return self.right.contains(target)
      else:
        return False
    elif target < self.value:
      if self.left:
        return self.left.contains(target)
      else:
        return False

  def get_max(self):
    if self.right == None:
      rnode = self.value
    else:
      rnode = self.right.get_max()
    return max(self.value, rnode)


  def for_each(self, cb):
    pass