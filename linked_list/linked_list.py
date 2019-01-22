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
    node = Node(value)
    if self.tail is not None:
        self.tail.set_next(node)
    else:
        self.head = node
    self.tail = node

  def remove_head(self):
    if self.head is not None:
     prev_val = self.head.value
     self.head = self.head.get_next()
     if self.head is None:
       self.tail = None

     return prev_val
    else:
      return None

  def contains(self, value):
    #set the current node to the head
    curr_node = self.head
    while True:
      #if the node is null, return false
      if curr_node is None:
        return False
      #else if the node's value matches the query value, return true
      elif curr_node.value == value:
        return True
      # otherwise, set the current node to the tail and start from step 1
      else:
        curr_node = curr_node .next_node

  def get_max(self):
    if self.head is None:
      return None
    curr_max = self.head
    curr_node = self.head

    while True:
      if curr_node is None:
        return curr_max.get_value()
      elif curr_node.get_value() > curr_max.get_value():
        curr_max = curr_node

      curr_node = curr_node.get_next()
