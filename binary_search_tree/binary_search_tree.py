class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value <= self.value:
      if self.left:
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
    else:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)

  def contains(self, target):
    if self.value == target:
      return True
    
    if target < self.value: 
      if self.left:
        return self.left.contains(target)
      else:
        return False
    else:
      if self.right:
        return self.right.contains(target)
      else:
        return False


  def get_max(self):
    pass


bst = BinarySearchTree(20)
bst.insert(19)
bst.insert(22)
bst.insert(10)
bst.insert(40)


print(bst.contains(10))