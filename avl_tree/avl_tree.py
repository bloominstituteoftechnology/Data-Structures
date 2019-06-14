"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
  def __init__(self, node=None):
    self.node = node
    # init height to -1 because of 0-indexing
    self.height = -1
    self.balance = 0

  """
  Display the whole tree. Uses recursive def.
  """
  def display(self, level=0, pref=''):
    self.update_height()  # Update height before balancing
    self.update_balance()
    
    if self.node != None: 
      print ('-' * level * 2, pref, self.node.key,
        f'[{self.height}:{self.balance}]',
        'L' if self.height == 0 else ' ')
      if self.node.left != None:
        self.node.left.display(level + 1, '<')
      if self.node.right != None:
        self.node.right.display(level + 1, '>')

  """
  Computes the maximum number of levels there are
  in the tree
  """
  def update_height(self, max_height = -1):
      # First I need a variable to store the max_number in
      # Then I need to create a while loop
        # Inside the while loop, whenever I hit the end_number of a branch, I need to subtract the max_number by 1 and go up 1, then see if there is another branch to go down. If not, I repeat the process until I am at the root with no new way down.
      # This reminds me of a binary search. I can just use recursion to keep going down, adding += to max number and then at the end returning max_number
        # So to do it this way, I would need to make a base case - the base case is when the algorithm can no longer go right or left.
    current = self.node
    
    if current == self.node:
        max_height = 0
    
    if not current.left and not current.right:
        if current == self.node:
            self.height = 0
        elif self.node == None:
            return -1
        return max_height
  
    elif current.right or current.left:
        max_height += 1
        if current.right:
            max_height += current.right.update_height(max_height)
        else:
            max_height += current.left.update_height(max_height)
        if max_height > self.height:
            self.height = max_height
    return max_height
  """
  Updates the balance factor on the AVLTree class
  """
  def update_balance(self):
    return (self.node.left.update_height() - self.node.right.update_height())
      
    pass

  """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent. 
  """
  def left_rotate(self):
      
    old_node = self.node
    self.node = self.node.right
    self.node.left = old_node


  """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent. 
  """
  def right_rotate(self):
    old_node = self.node
    self.node = self.node.left
    self.node.right = old_node

  """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """
  def rebalance(self):
    # Verify whether or not there is an unbalanced portion of the tree.
    # If not, we're done
    # If so, store the node and then balance the tree from the node that starts the imblanace.
    
    
  """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """
  def insert(self, key):
    pass
