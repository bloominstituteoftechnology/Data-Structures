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
    elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)    

  def contains(self, target):
    if self.value == target:
      return True
    elif self.value > target:
      if self.left is None:
        return False
      return self.left.contains(target)
    elif self.value < target:
      if self.right is None:
         return False
      return self.right.contains(target)

  def get_max(self):
    current_value = self
    max_value = 0
    
    while current_value:
      max_value = current_value.value
      current_value = current_value.right
    return max_value


  def for_each(self, cb):	  def for_each(self, cb):
    cb(self.value)
    if self.left and self.left is not None:
        self.left.for_each(cb)
    if self.right and self.right is not None:
        self.right.for_each(cb)

 