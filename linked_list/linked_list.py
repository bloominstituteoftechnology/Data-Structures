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
    # create a new node
    new_node = Node(value)
    # If the LL is not empty
    if self.tail:
      # Then set the tail's next to the new node
      self.tail.set_next(new_node)
      # self.tail = new_node #needed?
    else:
      # If it's empty, set the new node to the head
      self.head = new_node
    # Set the LL's to the new node
    self.tail = new_node

  def remove_head(self):
    new_head = self.head
    removed_head = None
    # Check to see if none
    if self.head:
      # set the head nodes next node value to a temp var
      new_head = self.head.next_node
      if new_head == None:
          self.tail = None
      removed_head = self.head.value
      # then set head to the temp
      self.head = new_head
      return removed_head
    
  def contains(self, value):
    # Set the current node to the head
    curr_node = self.head
    while curr_node:
      # 1. If the node is null, return False
      if curr_node is None:
        return False
      # 2. Else, if the node's value matches the query value, return True
      elif curr_node.get_value() == value:
        return True
      # 3. Otherwise, set the current node to the tail and start from step 1
      else:
        curr_node = curr_node.get_next()

  def get_max(self):
    # Check to see if none
    if not self.head:
      return None
    # Set the current node as max value (a temp var)
    curr_node = self.head.get_next()
    max_value = self.head.get_value()
    # step though each node and compare
    while curr_node:
      # if its bigger, set max to the bigger value
      if curr_node.get_value() > max_value:
        max_value = curr_node.get_value()
      curr_node = curr_node.get_next()
    return max_value

