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
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = self.tail.next_node

  def remove_head(self):
    removed = self.head
    if self.head == None:
      return None
    elif self.head.next_node == None:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next_node
    return removed.value

  def contains(self, value):
    if self.head == None:
      return False
    else:
      node = self.head
      while node is not None:
        if node.value == value:
          return True
        node = node.next_node
      return False

  def get_max(self):
    if self.head == None:
      return None
    else:
      start = self.head
      largest = self.head.value
      while start:
        if start.value > largest:
          largest = start.value
        start = start.next_node
      return largest