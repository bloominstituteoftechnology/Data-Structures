class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    newTreeNode = BinarySearchTree(value)
    # From the root go to the left side of the tree
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
  
  def contains(self, target):
    pass

  def get_max(self):
    pass
if __name__ == '__main__':
  tree = BinarySearchTree(4)
  tree.insert(3)
  tree.insert(2)
  tree.insert(7)
  tree.insert(8)
  tree.insert(5)
  print(tree.right.left.value)

  