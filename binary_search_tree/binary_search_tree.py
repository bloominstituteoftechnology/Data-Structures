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
    current = self
    while True:
      if current is None:
        return False
      if target == current.value:
        return True
      if target > current.value:
        current = current.right
      else:
        current = current.left

  def get_max(self):
    current = current.right
    while True:
      if current.right is None:
        return current.value

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

arr = [1,4,6,5,2,3,8]

bst = BinarySearchTree(0)

for i in arr:
  bst.insert(i)

for i in range(min(arr), max(arr)):
  if bst.contains(i)!= True:
    print(i)
    break
