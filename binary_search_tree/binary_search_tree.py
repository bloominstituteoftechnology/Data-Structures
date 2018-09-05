class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    newNode = BinarySearchTree(value)
    if value < self.value:
      if self.left == None:
        self.left = newNode
      else:
         self.left.insert(value)
    elif value >= self.value:
      if self.right == None:
        self.right = newNode
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if target < self.value:
      if self.left:
        if self.left.contains(target):
          return True
    else:
      if self.right:
        if self.right.contains(target):
          return True
    return False

  def get_max(self):
    if not self:
      return null
    maxVal = self.value
    current = self
    while(current):
      if current.value > maxVal:
        maxVal = current.value
      current = current.right
    return maxVal

