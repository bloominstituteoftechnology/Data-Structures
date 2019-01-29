class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == value:
      return False
    elif self.value > value:
      if self.left:
        return self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
    else:
      if self.right:
        return self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)
        return True
      

  def contains(self, target):
    mid = target[len(target) // 2]
    
    if len(target) == 0 or (len(target) == 1 and target[0] != self.value):
      return False

    if self.value == mid:
      return True
    elif self.value < mid:
      return BinarySearchTree.contains(target[:len(target) // 2], self.value)
    elif self.value > mid:
      return BinarySearchTree.contains(target[len(target) // 2 + 1], self.value)
   

  def get_max(self):
    pass


tree_test = BinarySearchTree(5)
tree_test.insert(10)
print(tree_test.contains([1,2]))
print(tree_test.insert(15))