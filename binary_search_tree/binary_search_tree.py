class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    node = self
    print(f"Node: {self.value}  Left: {self.left}  Right: {self.right}")
    while node != None:
      if value > node.value:
        if node.right == None:
          node.right = BinarySearchTree(value)
          node = None
        else:
          node = self.right
          print(f"Next Node: {node.value}\n")
      if value < node.value:
        if node.left == None:
          node.left = BinarySearchTree(value)
          node = None
        else:
          node = self.left
          print(f"Next Node: {node.value}\n")
  def contains(self, target):
    pass

  def get_max(self):
    pass
