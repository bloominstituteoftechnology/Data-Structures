class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current_node = self
    # while True: ##  First Pass Solution <-- Actual Insanity
    #   if current_node.right == None and current_node.left == None:
    #     current_node.right = BinarySearchTree(value)
    #     break
    #   elif current_node.right == None:
    #     if value >= current_node.left.value:
    #       current_node.right = BinarySearchTree(value)
    #       break
    #     else:
    #       current_node = current_node.left
    #   elif current_node.left == None: 
    #     if value <= current_node.right.value:
    #       current_node.left = BinarySearchTree(value)
    #       break
    #     else:
    #       current_node = current_node.right
    #   elif value >= current_node.right:
    #     current_node = current_node.right
    #   else:
    #     current_node = current_node.left


  def contains(self, target):
    pass

  def get_max(self):
    pass

bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)

print(bst.value)
print(bst.right.value)
print(bst.left.value)
print(bst.right.right.value)

