class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
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
      if not self.right:
        return False
      else:
        self.right.contains(target)
    elif target < self.value:
      if not self.left:
        return False
      else self.left.contains(target)    

  def get_max(self):
    if self.right is None:
      return self.value
    else:
      #Can I just call get max in this fashion or do I need to pass in an argument- self?
      self.right.get_max()  

  def for_each(self, cb):
    pass
