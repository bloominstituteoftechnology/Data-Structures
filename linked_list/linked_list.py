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
    if self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node
      self.tail.next_node = None

  def remove_head(self):
    removed = self.head
    if self.head:
      if not self.head.next_node:
        self.head = self.head.next_node
        self.tail = None
      else:
        self.head = self.head.next_node
      # self.tail = None
      return removed.value

  def contains(self, value):
    if self.head:
      search_node = self.head
      while search_node is not None:
        if search_node.value == value:
          return True
        search_node = search_node.next_node
      return False
    

  def get_max(self):
    if self.head:
      max_value = self.head.value
      curr_node = self.head
      while curr_node is not None:
        if curr_node.value > max_value:
          max_value = curr_node.value
        curr_node = curr_node.next_node
      return max_value
