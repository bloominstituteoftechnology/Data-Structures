class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # 1. Create a new tree to add
    # 2. If the new tree is less than the current trees value, go left
    # 2-1. If there is no left node, set the left node to the new tree
    # 2-2. Otherwise call insert on the current left node with the value to add (Recursively)
    # 3. If the new tree is greater than the current trees value, go right
    # 3-1. If there is no right node, set the right node to the new tree
    # 3-2. Otherwise call insert on the current right now with the value to add (Recursively)
    tree_to_add = BinarySearchTree(value) #1

    if tree_to_add.value < self.value: #2
      if self.left is None: #2-1
        self.left = tree_to_add
      else:
        self.left.insert(tree_to_add.value) #2-2
    elif tree_to_add.value > self.value: #3
      if self.right is None: #3-1
        self.right = tree_to_add
      else:
        self.right.insert(tree_to_add.value) #3-2

  def contains(self, target):
    pass

  def get_max(self):
    pass
