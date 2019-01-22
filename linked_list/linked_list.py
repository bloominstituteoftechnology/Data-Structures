"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node # pointer

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
    node = Node(value)
    # if the LL is not empty
    if self.tail is not None: 
      # set the tails next to the new node
      self.tail.set_next(node)
    else:
      # if it id empty set the new node to head
      self.head = node
    # set the LL tail to the new node
    self.tail = node

  def remove_head(self):
    # check if the head is not none
    if self.head is not None:
      # set the head bodes next node value to a temp var
      old_head = self.head
      # del the head node
      del(self.head)
      #then set head to that temp
      self.head = old_head.next_node
      print(self.head)
      if self.head is None:
        self.tail = None
      return old_head.value
    

  def contains(self, value):
    # set the current node to the head
    curr_node = self.head
    while True:
    # if the node is null return false
      if curr_node is None:
        return False
      # else if the node value matches query value return true
      elif curr_node.value == value:
        return True
      # otherwise set currents node to the tail
      else:
        curr_node = curr_node.next_node

  def get_max(self):
    # set the current node to the head
    curr_node = self.head
    # set max to None
    max_value = None
    while curr_node: 
      # if there current none value is greater
      if max_value is None or curr_node.get_value() > max_value:
        # set max to current
        max_value = curr_node.get_value()
      # set current to next node to move on to the next node
      curr_node = curr_node.get_next()
    return max_value