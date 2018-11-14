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
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
    self.tail = new_node

  def remove_head(self):
    if not self.head:
      return None
    else:
      return self.head.value

  def contains(self, value):
    while self.head:
      if self.head.value == value:
        return True
      else:
        self.head = self.head.next
    return False

  def get_max(self, value):
    values = []
    while self.head:
      top.append(self.head)
      self.head = self.head.next
    return max(values)
