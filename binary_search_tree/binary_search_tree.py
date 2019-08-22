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
    if value < self.value:
      #Go Left
      if not self.left:
        #add as leaf
        self.left = BinarySearchTree(value)
      else:
        #check again
        self.left.insert(value)
    else:
      #Go Right
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    # Searching a key
    # To search a given key in Binary Search Tree, we first compare it with root, 
    # if the key is present at root, we return root. If key is greater than root's 
    # key, we recur for right subtree of root node. Otherwise we recur for left 
    # subtree.
    if self.value == target:
      return True
    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    # Keep going right until you find a node without a child to the right
    if not self:
      return None
    else:
      if not self.right:
        return self.value
      else:
        return self.right.get_max()

  def for_each(self, callback):
    # We need to traverse the tree similar to how the print works in the demo
    # For each value append it to the array
    
    # Call the function
    callback(self.value)
    if self.left:
      self.left.for_each(callback)
    if self.right:
      self.right.for_each(callback)