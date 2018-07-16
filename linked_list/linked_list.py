"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    # setting value to value
    self.value = value
    # checking for and setting next node value
    self.next_node = next_node

  def get_value(self):
    # returns value of current node
    return self.value

  def get_next(self):
    # get next returns next nodes value if exists
    return self.next_node

  def set_next(self, new_next):
    # sets the value of next node to access if exists
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    # sets value of node to new_node
    new_node = Node(value)
    if self.head == None:
      # initializes head node's value if none
      self.head = new_node
      # initializes tail node's value to be the same as head while only 1 node exists
      self.tail = new_node
    else:
      # if head node exists then we call set_next(new_node) on tail
      self.tail.set_next(new_node)
      # and set new tail node to be new_node
      self.tail = new_node
    # returns new_node's value
    return new_node

  def remove_head(self):
    if self.head == None:
      # if there is no head to remove, we return None
      return None
    # if there is a head we set removed_head to equal the current heads value
    removed_head = self.head.get_value()
    # then we set head to the next value
    self.head = self.head.get_next()
    # returns removed head's value
    return removed_head

  def contains(self, value):

    # sets the current node to the current head's value
    current_node = self.head
    if current_node == None:
      # if there is no value return False
      return False
    elif current_node.get_value() == value:
      # if current_node.get_value() == value return True
      return True
    
    while current_node.get_next() != None:
      # sets current_node's value to next node value
      current_node = current_node.get_next()
      if current_node.get_value() == value:
        # checks to see if current_node is equal to value and returns True
        return True
    # if those conditions are never met, return False
    return False

  def get_max(self):
    # sets current_node's value to head node
    current_node = self.head
    if current_node == None:
      #  if no value then return None
      return None
    # sets max_node's value to current head node's value
    max_node = self.head.get_value()
    
    while current_node.get_next() != None:
      # sets current_node to next node
      current_node = current_node.get_next()
      # sets current_value to current_node's value
      current_value = current_node.get_value()
      if max_node < current_value:
        # if max_node is less than the current_value, set max_node to equal current_value
        max_node = current_value
    # return max_node value
    return max_node

