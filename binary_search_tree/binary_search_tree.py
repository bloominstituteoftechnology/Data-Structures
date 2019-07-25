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
        self.right =BinarySearchTree(value)
      else:
        self.right.insert(value)
    pass

  def contains(self, target):

    current = self
    while True:
      if target==current.value:
        return True
      elif target<current.value:
        if current.left==None:
          return False
        else:
          current = current.left
      else:
        if current.right==None:
          return False
        else:
          current = current.right

    pass

  def get_max(self):
    current=self
    while current.right:
      current=current.right
    return current.value

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

    pass