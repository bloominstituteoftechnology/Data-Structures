class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # def insert(self, value):
  #   if self.value == value:
  #     return False
  #   elif self.value > value:
  #     if self.left:
  #       return self.left.insert(value)
  #     else:
  #       self.left = BinarySearchTree(value)
  #   else:
  #     if self.right:
  #       return self.right.insert(value)
  #     else:
  #       self.right = BinarySearchTree(value)
  #       return True
      if

  def contains(self, target):
    if target > self.value:
      # search left side
    elif target < self.value:
      # search right side
   

  def get_max(self):
    pass


tree_test = BinarySearchTree(5)
tree_test.insert(10)
print(tree_test.contains([1,2,5.9]))
print(tree_test.insert(15))