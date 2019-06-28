class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # 1. Check if the new node's value is less than? Go left
    #   a. Is there a child? If not, insert value
    #   b. If yes, repeat process
    # 2. If value is greater than? Go right
    #   a. Is there a child? If not, insert value
    #   b. Repeat the process

    # Leaves are the 'base case' to stop recursion

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
    if self.value == target:
      return True

    if target < self.value:
      # Search left
      if not self.left:
        return False

      return self.left.contains(target)
    else:
      # Search right
      if not self.right:
        return False

      return self.right.contains(target)


  def get_max(self):
    while self.right is not None:
      max = self.value
      self = self.right

    max = self.value
    return max


  def for_each(self, cb):
    if self.left:
      self.left.for_each(cb)
    cb(self.value)
    if self.right:
      self.right.for_each(cb)
    

