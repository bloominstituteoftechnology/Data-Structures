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
    # create the node
    # if tail != none | set next to node
    # if tail is none | set head as node
    # set the tail as node 
    pass

  def remove_head(self):
    # if head != none
    # get the next node from the head save to a temp variable
    # set the temp variable to the head
    pass

  def contains(self, value):
    # while tail is true
    # check if value matches node
    # go to the next node
    pass

  def get_max(self):
    # set a results variable
    # while tail is true
    # if value is > results | result = value
    pass
