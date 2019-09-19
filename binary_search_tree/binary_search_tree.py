import sys
import random
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class node:
  def __init__(self, value = None):
    self.value = value
    self.left_child = None
    self.right_child = None 

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    #no root node
    if self.root == None:
      self.root = node(value)
    #else we want to insert node
    else:
      self._insert(value, self.root)

  def _insert(self, value, current_node):
    #if passed value is less than the current node value
    if value < current_node.value:
      #Case 1
      if current_node.left_child == None:
        current_node.left_child = node(value)
      else:
        self._insert(value, current_node.left_child)

    #if value is greater than current node value
    elif value > current_node.value:
      #Case 2
      if current_node.right_child == None:
        current_node.right_child = node(value)
      else:
        self._insert(value, current_node.right_child)

    #the same value is already in tree
    else:
      print ("Value already exist in the tree")

  def print_tree(self):
    if self.root != None:
      self._print_tree(self.root)
  
  def _print_tree(self, current_node):
    if current_node != None:
      self._print_tree(current_node.left_child)
      print (f"Current Node {current_node.value}")
      self._print_tree(current_node.right_child)

  def contains(self, target):
    if self.root != None:
      return self._contains(target, self.root)
    else:
      return False

  def _contains(self, target, current_node):
    if target == current_node.value:
      return True
    elif target < current_node.value and current_node.left_child != None:
      return self._contains(target, current_node.left_child)
    elif target > current_node.value and current_node.right_child != None:
      return self._contains(target, current_node.right_child)
    else:
      return False


  def get_max(self):
    if self == None:
      return "Tree is empty"
    
    current_max = self.root
    print('value of the right child')

    while current_max.right_child:
      print("max", current_max.value)
      current_max = node(current_max.right_child.value)

    return current_max.value

  def for_each(self, cb):
    pass


  # DAY 2 Project -----------------------

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_print(self, node):
      pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
  def bft_print(self, node):

    queue = []

    if node:
        queue.append(node)

    while len(queue) > 0:
      print(queue[0].value)
      current_node = queue[0]

      if current_node.left_child:
        queue.append(current_node.left_child)

      if current_node.right_child:
        queue.append(current_node.right_child)

      queue.pop(0)

     


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
  def dft_print(self, node):
      pass

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
      pass

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
      pass



tree = BinarySearchTree()

tree.insert(3)
tree.insert(2)
tree.insert(10)
tree.insert(6)
tree.insert(1)

tree.print_tree()

print(tree.contains(40))

print(tree.get_max())

print(tree.bft_print(tree.root))

 