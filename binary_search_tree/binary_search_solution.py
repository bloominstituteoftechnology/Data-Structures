class BinarySearchTree:
      def __init__(self, value):
    # the value at the current node
    self.value = value
    # reference to this node's left child
    self.left = None
    # reference to this node's right child
    self.right = None

  def insert(self, value):
    # wrap the value in a new tree node
    new_tree = BinarySearchTree(value)
    # check if the new node's value is less than our current node's value
    if value < self.value:
      # if there's no left child here already, place the new node here
      if not self.left:
        self.left = new_tree
      else:
        # otherwise, repeat the process!
        self.left.insert(value)
    # check if the new node's value is greater than or equal to our current node's value
    elif value >= self.value:
      # if there's no right child here already, place the new node here
      if not self.right:
        self.right = new_tree
      else:
        # otherwise, repeat the process!
        self.right.insert(value)

  def contains(self, target):
    # if the value of the current node we're looking at matches the target, we've found a match!
    if self.value == target:
      return True
    # if there's a left child, call its contains method to repeat the whole process
    if target < self.value:
      if self.left:
        return self.left.contains(target):
    # if there's a right child, call its contains method to repeat the whole process
    else:
      if self.right:
        return self.right.contains(target):
    # if we got here, then the we've looked through the entire tree and didn't find our target
    return False

  def get_max(self):
    # no point in doing anything if our tree is empty
    if not self:
      return None

    # Recursive approach
    # if not self.right:
    #   return self.value
    # return self.right.get_max()
    
    # initialize max_value variable; this will be updated as we traverse the tree
    max_value = self.value
    # get a reference to the node we're currently at; update this variable as we traverse the tree
    current = self
    # check to see if we're still at a valid tree node
    while current:
      # if current value is greater than max_value, update the max_value
      if current.value > max_value:
        max_value = current.value
      # move on to the next right node in the tree
      current = current.right
    return max_value