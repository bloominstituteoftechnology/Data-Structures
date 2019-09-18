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
    pass

  def for_each(self, cb):
    pass



tree = BinarySearchTree()

tree.insert(3)
tree.insert(2)
tree.insert(10)
tree.insert(6)
tree.insert(1)

tree.print_tree()

print(tree.contains(40))

 