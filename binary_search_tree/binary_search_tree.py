class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current_tree = self
    placed = False
    while not placed:
      # Passed in value is smaller than current_tree value
      if value < current_tree.value:
        if current_tree.left == None:   # Place it there if no node present
          current_tree.left = BinarySearchTree(value)
          placed = True
        else:
          current_tree = current_tree.left  # Or move one tree down
      # Passed in value is greater than (or equal to) current_tree value
      else:
        if current_tree.right == None:
          current_tree.right = BinarySearchTree(value)
          placed = True
        else:
          current_tree = current_tree.right

  def contains(self, target):
    current_tree = self
    while True:
      if current_tree == None:
        return False
      if current_tree.value == target:
        return True
      # Passed in value is smaller than current_tree value
      if target < current_tree.value:
        current_tree = current_tree.left 
      # Passed in value is greater than (or equal to) current_tree value
      else:
        current_tree = current_tree.right

  def get_max(self):
    current_tree = self
    max_val = current_tree.value
    while True:
      if current_tree.value > max_val:
        max_val = current_tree.value
      if current_tree.right == None:
        return max_val
      else:
        current_tree = current_tree.right
  
