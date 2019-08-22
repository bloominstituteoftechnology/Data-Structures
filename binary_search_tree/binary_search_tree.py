class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # Insertion of a key, a new key is always inserted at leaf. 
    # We start searching a key from root 
    # till we hit a leaf node. Once a leaf node is found,
    # the new node is added as a child of the leaf node.
    if self.value:
      if self.value > value:
        
  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, callback):
    pass