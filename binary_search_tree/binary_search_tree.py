class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    if new_node.value >= self.value:
      if not self.right:
        self.right = new_node
      else:
        self.right.insert(value)
    else:
      if not self.left:
        self.left = new_node
      else:
        self.left.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass


tree = BinarySearchTree(8)
tree.insert(10)
print(tree.value)
print(tree.right.value)

