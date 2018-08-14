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

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next_node

  def add_to_tail(self, value):
    node = Node(value)
    if self.head:
      self.tail.next_node = node
    else:
      self.head = node
    self.tail = node

  def remove_head(self):
    prev_value = None

    if not self.head:
      return None
    elif self.head is self.tail:
      prev_value = self.head.value
      self.head = None
      self.tail = None
    else:
      prev_value = self.head.value
      self.head = self.head.next_node

    return prev_value

  def contains(self, value):
    for node in self:
      if node.value is value:
        return True
    return False

  def get_max(self):
    if not self.head:
      return None

    max = self.head.value

    for node in self:
      if node.value > max:
        max = node.value

    return max
