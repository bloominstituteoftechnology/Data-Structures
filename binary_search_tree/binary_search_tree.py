class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    bst_node = BinarySearchTree(value)
    parent = self
    while True:
        if value < parent.value:
            if parent.left:
                parent = parent.left
            else:
                parent.left = bst_node
                return
        else:
            if parent.right:
                parent = parent.right
            else:
                parent.right = bst_node
                return

  def contains(self, target):
    parent = self
    while parent:
        if target < parent.value:
            parent = parent.left
        elif target == parent.value:
            return True
        else:
            parent = parent.right
    return False

  def get_max(self):
    parent = self
    while parent.right:
        parent = parent.right
    return parent.value