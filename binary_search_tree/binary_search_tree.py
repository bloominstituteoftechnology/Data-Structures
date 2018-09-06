class BinarySearchTree:


  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.max = value

  def insert(self, value):
    
    newTreeNode = BinarySearchTree(value)
    while True:
      if self.left == None and self.value >= newTreeNode.value:
        self.left = newTreeNode
        return True
      
      if self.right == None and self.value < newTreeNode.value:
        self.right = newTreeNode
        return True
      if self.value >= newTreeNode.value:
        self = self.left
      else:
        self = self.right
  

  def contains(self, target):
    while self:
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
    maxValue = self.value
    while self:
      if self.value > maxValue:
        maxValue = self.value
      self = self.right
    return maxValue
  

if __name__ == '__main__':
  tree = BinarySearchTree(5)

  