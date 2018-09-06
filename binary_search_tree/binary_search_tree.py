class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    curr = self
    parent = None
    while curr:
      parent = curr
      if value < curr.value:
        curr = curr.left
      else:
        curr = curr.right
    curr = BinarySearchTree(value)

    if value < parent.value:
      parent.left = curr
    else:
      parent.right = curr
  def contains(self, target):
    pass

  def get_max(self):
    pass
