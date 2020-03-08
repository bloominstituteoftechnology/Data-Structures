from queue import Queue

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
    curr_node = BinarySearchTree(value)
    if value <= self.value:
      if curr_node.left is None:
        curr_node.left = curr_node
    if value > self.value:
      if curr_node.right is None:
        curr_node.right = curr_node

    pass

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def bft(self):
    queue = Queue
    #queue => stack