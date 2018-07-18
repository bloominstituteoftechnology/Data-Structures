class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # Wrap the value in a BinarySearchTree instance
    new_tree = BinarySearchTree(value)
    # Check and see if the new node's value is less than our current node's value
    if value < self.value:
      # If there is no left child here already, place the new node here
      if not self.left:
        self.left = new_tree
      # There is a node there
      else:
        # Repeat the whole process
        self.left.insert(value)
    # The value is >= to the current value
    else:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)
        
  def contains(self, target):
    # If the value of the current node matches the target, we're done.
    if self.value == target:
      return True
    # If value < the current node's value, call contains on the left subtree
    if target < self.value:
      # Check if self.left exists.
      if self.left:
        if self.left.contains(target):
          return True
    else:
      if self.right:
        if self.right.contains(target):
          return True
    # Our tree doesn't contain the target.
    return False

  def get_max(self):
    # No point in doing anything if our tree is empty.
    if not self:
      return None
    # Check to see if we have a child to the right.
    if not self.right:
      return self.value
    # We still have more children to the right.
    return self.right.get_max()
