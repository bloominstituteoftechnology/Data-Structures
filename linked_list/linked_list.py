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
    if self.tail == None:
      if self.head == None:
        self.head = new_node
      else:
        self.head.next_node = new_node
    else:
      self.tail.next_node = new_node
    self.tail = new_node

  def remove_head(self):
    if self.head != None:
      original_head = self.head
      self.head = self.head.next_node
      return original_head.value
    return None

  def contains(self, value):
    current_head = self.head
    while current_head != None:
      if current_head.value == value:
        return True
      current_head = current_head.next_node
    return False

  def get_max(self):
    if self.head == None:
      return None
    max_node = self.head.value
    current_node = self.head
    while current_node != None:
      if current_node.value > max_node:
        max_node = current_node.value
      current_node = current_node.next_node
    return max_node