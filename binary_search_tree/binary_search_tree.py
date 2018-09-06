class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    node = self

    while(node):

      last_node = node
      if(node.value <= value):
        node = node.right
      else:
        node = node.left

    if(last_node.value <= value):
      last_node.right = BinarySearchTree(value)
    else:
      last_node.left = BinarySearchTree(value)
      

  def contains(self, target):

    node = self
    while(node):
      if(node.value == target): return True
      elif(node.value < target): node = node.right
      else: node = node.left
      
  def get_max(self):
    node = self
    while(node):
      last_node = node
      node = node.right

    return last_node.value