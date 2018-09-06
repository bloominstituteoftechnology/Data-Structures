class BinarySearchTree:
  def __init__(self, value):
    #current Node value
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    #check if value is greater than current value, then go right, else go left
    if value >= self.value:
      #if there's node on the right, then assign new Node to right
      if (not self.right):
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    else:
      if (not self.left):
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

  def contains(self, target):
    current = self
    found = False
    while (current and not found):
      if target < current.value:
        current = current.left
      elif target > current.value:
        current = current.right
      else:
        found = True
    return found

  def get_max(self):
    if self.right == None:
      return self.value
    return self.right.get_max()
