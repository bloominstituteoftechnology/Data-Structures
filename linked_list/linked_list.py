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
    new_node = Node(value)
    # if there is no head, set node to head and tail
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
    # otherwise use set_next method on current tail node and set a new tail
      self.tail.set_next(new_node)
      self.tail = new_node

  def remove_head(self):
    # edge case for lists with 0 items
    if self.head == None:
      return None
      # edge case for lists with 1 item
    if self.head.get_next() == None:
      pop_head = self.head.get_value()
      self.head = None
      self.tail = None
      return pop_head
      # base case
    else:
      pop_head = self.head.get_value()
      self.head = self.head.get_next()
      return pop_head

  def contains(self, value):
    # edge case for empty head
    if self.head == None:
      return False
    
    # base case
    current = self.head
    while current:
      if current.get_value() == value:
        return True
      current = current.get_next()
    return False

  def get_max(self):
    if self.head == None:
      return None

    if self.head.get_next() == None:
      return self.head.get_value()
    max_value = self.head.get_value()
    current = self.head
    while current:
      if current.get_value() > max_value:
        max_value = current.get_value()
      current = current.get_next()
    
    return max_value
      
