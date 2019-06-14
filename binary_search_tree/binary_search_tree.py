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
    if target == self.value:
      return True
    elif self.right is None and self.left is None:
      return False
    else:
      if self.left is not None:
        if self.left.contains(target):
          return True
      if self.right is not None:
        if self.right.contains(target):
          return True

  def get_max(self):
    if self.right is None:
      return self.value
    else:
      return self.right.get_max()

  def for_each(self, cb):
      cb(self.value)
      if self.left:
        self.left.for_each(cb)
      if self.right:
        self.right.for_each(cb)

arr = [ 1, 4, 6, 5, 2, 3, 8]


bst = BinarySearchTree(0)

for i in arr:
  bst.insert(i)

for i in range(min(arr), max(arr)):
  if bst.contains(i)!= True:
    print(i)
    break
