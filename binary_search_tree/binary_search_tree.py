class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current = self
    while True:
      if value < current.value:
        if current.left == None:
          current.left = BinarySearchTree(value)
          break
      elif value > current.value:
        if current.right == None:
          current.right = BinarySearchTree(value)
          break

  def contains(self, target):
    # if target > self.value:
    #   # search left side
    # elif target < self.value:
      # search right side
   pass

  def get_max(self):
    pass


# tree_test = BinarySearchTree(5)
# print(tree_test.insert(10))
# print(tree_test.left.value)