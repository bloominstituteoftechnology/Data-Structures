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
    if self.tail is None:
      node_one = Node(value)
      self.head = node_one
      self.tail = node_one
    else:
      new_node = Node(value)
      self.tail.next_node = new_node
      self.tail = new_node
      self.tail.next_node = None

  def remove_head(self):
    if not self.head:
      return None
    if not self.head.next_node:
      head = self.head
      self.head = None
      self.tail = None
      return head.value
    else:
      value = self.head.value
      self.head = self.head.next_node
      return value
      


  def contains(self, value):
    if not self.head:
      return None
    current_node = self.head
    while current_node:
      if current_node.value == value:
        return True
      current_node = current_node.get_next()
    return False

  def get_max(self):
    if not self.head:
      return None
    max_value = self.head.value
    current_head = self.head.get_next()
    while current_head:
      if current_head.value > max_value:
        max_value = current_head.value
      current_head = current_head.next_node
    return max_value
  
