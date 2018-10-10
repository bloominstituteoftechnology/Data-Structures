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
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      self.tail.set_next(node)
      self.tail = node
      self.tail.set_next(None)

  def remove_head(self):
    if self.head == None:
      return None
    else:
      current_head = self.head.get_value()
    if self.head.get_next() != None:
        self.head = self.head.get_next()
    else:
        self.head = None
        self.tail = None
    return current_head

  def contains(self, value):
    if self.head == None:
      return None
    current = self.head
    if current.get_value() == value:
      return True
    while current.get_next() != None:
      current = current.get_next()
      if current.get_value() == value:
        return True
    return False

  def get_max(self):
    if self.head == None:
      return None
    current = self.head
    maximum = current.get_value()
    while current.get_next() != None:
      current = current.get_next()
      if current.get_value() > maximum:
        maximum = current.get_value()
    return maximum
