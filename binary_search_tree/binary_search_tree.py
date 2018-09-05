class BinarySearchTree:


  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.max = value

  def insert(self, value):
    
    # This method is only used for the get_max method
    self.set_max_value(value)

    newTreeNode = BinarySearchTree(value)
    while True:
      if self.left == None and self.value >= newTreeNode.value:
        self.left = newTreeNode
        return
      
      if self.right == None and self.value < newTreeNode.value:
        self.right = newTreeNode
        return
      if self.value >= newTreeNode.value:
        self = self.left
      else:
        self = self.right
  
  def set_max_value(self, value):
    if value > self.max:
      self.max = value

  def contains(self, target):
    while True:
      if self.value == target:
        return True
      
      if self.value >= target:
        if self.left == None:
          return False

        self = self.left

      else:
        if self.right == None:
          return False

        self = self.right
      
  def get_max(self):
    return self.max

if __name__ == '__main__':
  tree = BinarySearchTree(5)

  