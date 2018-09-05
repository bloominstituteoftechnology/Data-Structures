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
    new_node.set_next(None)
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      current_node = self.tail
      current_node.set_next(new_node)
      self.tail = new_node
    
  def remove_head(self):
    current = self.head
    if current is None:
      raise ValueError('Head undefined')
    self.head = current.get_next()
    current.set_next(None)

  def contains(self, value):
    current = self.head
    found = False
    while current and found is False:
      if current.get_value() == value:
        found = True
      else:
        current = current.get_next()
      if current is None:
        return found
    return found

  def get_max(self):
    current = self.head
    current_max = self.head.value
    found = False
    while current and found is False:
      current = current.get_next()
      if current is None:
        found = True
      if current.get_value() > current_max:
        current_max = current.get_value()
    
    return current_max
