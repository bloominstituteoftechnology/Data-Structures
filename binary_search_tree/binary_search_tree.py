class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    if value < self.value:
      if not self.left:
        self.left = new_node
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = new_node
      else:
        self.right.insert(value) 
    
  def contains(self, target):
    if self.value == target:
      return True
    elif target < self.value:
      if self.left:
       if self.left.contains(target):
        return True
    else:
      if self.right:
        if self.right.contains(target):
          return True
    return False  
  

  def get_max(self):
    pass


tree = BinarySearchTree(10)
tree.insert(3)
tree.insert(16)

print(tree.value)
tree.contains(77)