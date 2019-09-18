import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    #initialize left and right value to None
    self.value = value
    #reference to node's left child
    self.left = None
    #reference to node's right child
    self.right = None

  # Insert the given value into the tree
  def insert(self, value):
    #initialize new_tree as an instance of BinarySearchTree(value)
    new_tree = BinarySearchTree(value)
    #if value is less than self.value:
    if value < self.value:
      #if there's no left node, assert that self.left == new_tree
      if not self.left:
        self.left = new_tree
      else:
        #repeat the process
        self.left.insert(value)
    else:
      #if there's no right node value, assert that self.right == new_tree
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  # Return True if the tree contains the value
  # False if it does not
  def contains(self, target):
    #check to see if value of current node matches the target
    if self.value == target:
      return True
  
      #if value < the current node value, call contains on the left subtree
    if target < self.value:
      #check if self.left exists
      if self.left:
        #if self.left exists, check to see if it contains the target
        if self.left.contains(target):
          return True
    else:
      if self.right: #if self.right exists, check to see if it contains the target
        if self.right.contains(target):
          return True
    
    #if we get here our tree doesn't contain target
    return False

  # Return the maximum value found in the tree
  def get_max(self):
    if not self:
      return None

    max_value = self.value

    current = self

    while current:
      if current.value > max_value:
        max_value = current.value
      
      current = current.right
    return max_value



  # Call the function `cb` on the value of each node
  # You may use a recursive or iterative approach
  def r_for_each(self, cb):
    pass

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_print()
    pass

  # Print the value of every node, starting with the given node,
  # in a breadth first traversal
  def bft_print(node):
    pass

  # Print the value of every node, starting with the given node,
  # in a depth first traversal
  def dft_print(node):
    pass


  ########Stretch Goals#########
  # Note: Research may be required

  # Print In-order DFT
  def pre_order_dft(self, node):
      pass

  # Print Post-order DFT
  def post_order_dft(self, node):
    pass
  
