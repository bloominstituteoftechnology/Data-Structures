class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    cur = self
    parent = None
    while cur:
      parent = cur
      if value < cur.value:
        cur = cur.left
      else:
        cur = cur.right
    cur = BinarySearchTree(value)

  def contains(self, target):
    cur = self
    while cur:
      if target == cur.value:
          return True
      else:
          return False

  def get_max(self):
    cur = self
    parent = None
    while cur.right:
      parent = cur.right
      cur = 
    return cur.value
