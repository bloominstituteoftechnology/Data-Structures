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

    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = self.tail.get_next()
    
  def remove_head(self):
    if self.head is None:
      return None

    current = self.head

    if current == self.tail:
      self.tail = None

    self.head = self.head.get_next()

    return current.value

  def contains(self, value):
    if self.head is None:
      return None

    current = self.head
    found = False

    while current and found is False:
      if current.get_value() == value:
        found = True
      else:
        current = current.get_next()

    return found

  def get_max(self):
    if self.head is None:
      return None

    current = self.head
    current_max = current.get_value()

    while current is not None:
      if current.get_value() > current_max:
        current_max = current.get_value()
      else:
        current = current.get_next()

    return current_max
