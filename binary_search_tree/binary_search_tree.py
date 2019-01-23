class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    # The value at the top is the root node
    # The nodes with no children are leaf nodes
    # You can think of the binary tree as having multiple
    # levels, with each level downwards the total nodes increases = 2^n
      # All full binary search trees are complete
      # but not all complete trees are full
        # Complete meaning you have children
        # migrated to the left half of the tree
      # A height balanced tree is when the bottom leafs are not more than
      # two levels apart
    self.left = None
    # Everything to the left of the binary tree,
    #  the child nodes must be smaller than the parent node
    self.right = None
    # Everything to the right of the binary tree,
    # the child nodes must be bigger than the parent node

  def insert(self, value):
    branch = self.value #25
    root = BinarySearchTree(value) #81
    sub_tree = BinarySearchTree(value)
    # print(root.value)
    # print(branch)
    if root.value > branch:
      root.right = sub_tree
      # root.right.value = branch
      print(root.right.value)
    elif root.value < branch:
      root.left = sub_tree
      # root.left.value = branch
      print(root.left.value)
      


    pass

  def contains(self, target):
    pass

  def get_max(self):
    pass


