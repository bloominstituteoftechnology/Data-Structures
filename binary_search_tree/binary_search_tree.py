class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    root = self.value

    if value < root:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value >= root:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
       self.right.insert(value)


  def contains(self, value):
    root = self.value
    
    if value == root:
      return True
    elif value < root:
      if self.left == None:
        return False
      else:
        return self.left.contains(value)
    elif value >= root:
      if self.right == None:
        return False
      else:
        return self.right.contains(value)


  def get_max(self):
    if self.right == None:
      return self.value
    
    else:
      right_node = self.right
      max_value = self.value
      while right_node:
        max_value = right_node.value
        right_node = right_node.right
        print(max_value)
      return max_value
       

