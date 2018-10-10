class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    insertedTreeNode = BinarySearchTree(value)
    while True:
      if self.left == None and self.value >= insertedTreeNode.value:
        self.left = insertedTreeNode
        return True
      if self.right == None and self.value < insertedTreeNode.value:
        self.right = insertedTreeNode
        return True
      if self.value >= insertedTreeNode.value:
        self = self.left
      else:
        self = self.right

  def contains(self, target):
    pass

  def get_max(self):
    pass
