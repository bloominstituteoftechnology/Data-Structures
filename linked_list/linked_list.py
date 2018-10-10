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
    self.tail = new_node
    if self.head == None:
      self.head = new_node
      return
    last = self.head
    while (last.next_node):
      last = last.next_node
    last.next_node = new_node

  def remove_head(self):
    if self.head is not None:
      value = self.head.value
      if self.head.next_node is None:
        self.head = None
        self.tail = None
      if self.head:
        self.head = self.head.next_node
      return value

  def contains(self, value):
    if self.head == None:
      return False
    curr_node = self.head
    while (curr_node.next_node):
      if curr_node.value == value:
        return True
      curr_node = curr_node.next_node
    if curr_node.value == value:
      return True
    return False

  def get_max(self):
    if self.head == None:
      return None
    curr_node = self.head
    maximum = self.head.value
    while (curr_node.next_node):
      if curr_node.value > maximum:
        maximum = curr_node.value
      curr_node = curr_node.next_node
    if curr_node.value > maximum:
      maximum = curr_node.value
    return maximum

  def __iter__(self):
    node = self.head
    while (node):
      yield node
      node = node.next_node

