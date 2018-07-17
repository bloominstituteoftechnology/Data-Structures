"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    if self.head is None:
      self.head = Node(value)
      self.tail = self.head
    else:
      self.tail.next_node = Node(value)
      self.tail = self.tail.next_node

# Add to Tail: first check for a head, if none, your list is empty. Add your value - it is both head and tail.
# if there is a head, add the new value after the tail and the reset the tail to be your new value.
  
  def remove_head(self):
    if self.head == None:
      return None
    else:
      temp = self.head.value
      self.head = self.head.next_node
      return temp

# Remove head: if there is no head, then there is nothing to do.
# if there is one, make a temporary placeholder for the head. Reset the head to be the next node,
# then return the head.

  def contains(self, value):
    current = self.head
    while current is not None:
      if current.value == value:
        return True
      else:
        current = current.next_node
    return False

# Contains: the head is the starting position(current). If there is one, check the current value.
# if the current value is the value you're looking for, return it. If not, check the next node.
# Repeat as long as there are nodes to check.
# If you don't find anything, return false.

  def get_max(self):
    if self.head == None:
      return None
    maximum = self.head.value
    current = self.head
    while current is not None:
      if current.value > maximum:
        maximum = current.value
      current = current.next_node
    return maximum

# Get max: if there is no head, there is nothing to do. Return none.
# If there is one, the value of the current node will be the variable "maximum" 
# The value of the current head will be the variable "current"
# If the current head's value > the current maximum, then assign the value of the current maximum to the current node value
# Assign the value of the next node as the current node
# Keep going until you run out of things to check, and then return whatever the current maximum is.
