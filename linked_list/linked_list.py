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
    newest_node = Node(value)
    if self.tail == None:
      if self.head == None:
        self.head = newest_node
      else:
        self.head.next_node = newest_node
    else:
      self.tail.next_node = newest_node
    self.tail = newest_node

  def remove_head(self):
    if self.head != None:
      oldest_head = self.head
      self.head = self.head.next_node
      return oldest_head.value
    return None

  def contains(self):
    current = self.head
    while current != None:
      if current.value == value:
        return True
      current = current.next_node
    return False

  def get_max(self):
    pass
