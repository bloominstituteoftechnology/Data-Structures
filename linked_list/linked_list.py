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
    next_node = Node(value)

    if not self.head:
      self.head = next_node
      self.tail = next_node
    else:
      self.tail.set_next(next_node)
      self.tail = next_node

  def remove_head(self):
    if not self.head:
      return None
    else:
      removed_head = self.head
      if self.tail:
        if self.head == self.tail:
          self.head = None
          self.tail = None
        else:
          self.head = self.head.get_next()
      else:
        self.head = None
    return removed_head.get_value()

  def contains(self, value):
    curr_head = self.head
    while curr_head:
      if curr_head.get_value() == value:
        return True
      curr_head = curr_head.get_next()
    return False

  def get_max(self):
    curr_head = self.head
    maximum_value = None
    while curr_head:
      if maximum_value is None or curr_head.get_value() > maximum_value:
          maximum_value = curr_head.get_value()
      curr_head = curr_head.get_next()
    return maximum_value
