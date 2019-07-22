class BinarySearchTree:
  def __init__(self, value):
    # The value at the current Node
    self.value = value
    # Reference to this node's left child
    self.left = None
    # Reference to this node's right child
    self.right = None

  def insert(self, value):
  # `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.

  # Check if no current node
    if not self:
      return "Empty"
    # 1. Check if the new node's value is less than current node's value
    if value < self.value:
    #   a. Is there a child? If not insert new node
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
    #   b. Repeat process - Check if new node is greater or lesser than current node's value
        return self.left.insert(value)
    # 2. Check if new node's value is greater than current node's value
    if value >= self.value:
    #   a. Is there a child? If not insert new node
      if not self.right:
        self.right = BinarySearchTree(value)
    #   b. Repeat prcess
      else:
        return self.right.insert(value)

  def contains(self, target):
  # `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.

  # Check if no current node
    if not self:
      return "Empty"

    # 1. Check to see if target's value is the same as current node's value
    if target == self.value:
    #   a. If so return True
      return True

    # 2. Check to Left side of Tree
    if target < self.value:
    #   a. If you can't go further return False
      if not self.left:
          return False
      
      else:
    #   b. Continue down the Tree
        return self.left.contains(target)

    # 3. Check to Right side of Tree
    if target > self.value:
    #   a. If you can't go further return False
      if not self.right:
          return False

      else:
    #   b. Continue down the Tree
        return self.right.contains(target)

  def get_max(self):
  # `get_max` returns the maximum value in the binary search tree.

  # Check if no current node
    if not self:
      return "Empty"

  # Create variables for current node and a max value variable
    max_value = self.value
    current_node = self

  # Create while loop going to the right side of the tree
    while (current_node.right):
    # Set current node to the next node to the right
      current_node = current_node.right
    # Set max value variable to the current nodes value
      max_value = current_node.value

    # return max value variable
    return max_value

  def for_each(self, cb):
  # `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work. 

    # write callback with self.value as variable
    cb(self.value)

    # For the left side of the tree run callback on each node
    if self.left:
      self.left.for_each(cb)

    # For the right side of the tree run callback on each node
    if self.right:
      self.right.for_each(cb)