class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value == self.value:
        return
    elif value < self.value:
        if self.left == None:
            self.left = BinarySearchTree(value)
        else:
            self.left.insert(value)
    else:
        if self.right == None:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)

  def contains(self, value):
    if value == self.value:
        return True
    elif value < self.value:
        if self.left:
            return self.left.contains(value)
        else:
            return False
    else:
        if self.right:
            return self.right.contains(value)
        else:
            return False

  def get_max(self):
    # Returns the right most node of the BST.
    max_node = self
    while max_node.right:
        max_node = max_node.right
    return max_node
