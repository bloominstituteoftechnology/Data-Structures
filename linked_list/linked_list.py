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
    if self.head is None:
      self.head = node
      self.tail = node

    elif self.tail and self.head:
      old_tail = self.tail
      old_tail.set_next(node)
    self.tail = node

  def remove_head(self):
    if self.head is None:
      return None
    elif self.head.get_next() is None:
      current = self.head
      self.head = None
      self.tail = None
      return current.value
    else:
      current = self.head
      self.head = current.next_node
      current.next_node = None
      return current.value


  def contains(self, value):
    result = self.head
    while result is not None:
        if result.get_value() == value:
            return True
        else:
            result = result.get_next()
    return False

  def get_max(self):
    max_node = None
    current = self.head
    if current is not None:
         max_node = current.get_value()
    while current is not None:
        if current.get_value() > max_node:
             max_node = current.get_value()
        current = current.get_next()
    return max_node
