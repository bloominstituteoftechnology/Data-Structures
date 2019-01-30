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
          print(current.left.value)
          break
        else:
          current = current.left
          
      else:
        if current.right == None:
          current.right = BinarySearchTree(value)
          print(current.right.value)
          break
        else:
          current = current.right
          
          
        

  def contains(self, target):
    # if target > self.value:
    #   # search left side
    # elif target < self.value:
      # search right side
   pass

  def get_max(self):
    pass


tree_test = BinarySearchTree(5)
tree_test.insert(2)
tree_test.insert(3)
tree_test.insert(7)
tree_test.insert(6)
print(tree_test.right.value)