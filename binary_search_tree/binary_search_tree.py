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
    elif value > self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    # test if the value is the target
    # if not the target, test if value is less than
    # run co left value if it exists
    # if not less than, value is greater than
    # check right value if it exists
    if self.value == target:
      return True
    elif self.value < target:
      if self.right:
        print(self.right.value)
        self.right.contains(target)
    elif self.left:
      print(self.left.value)
      self.left.contains(target)
    return False

  def get_max(self):
    pass

  def for_each(self, cb):
    pass