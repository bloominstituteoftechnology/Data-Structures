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
    # new_node.next_node = None
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = self.tail.next_node



  def remove_head(self):
    old_head = self.head
    if old_head is None: # Empty Linked List
      return None
    elif old_head == self.tail:  # Only 1 val in Linked List
      self.head = None
      self.tail = None
      return old_head.get_value()
    else:                     # Two or more vals in Linked List
      self.head = self.head.get_next()
      return old_head.get_value()



  def contains(self, value):
    current = self.head
    while current:
      if current.get_value() == value:
        return True
      else:
        current = current.get_next()
    return False

  def get_max(self):
    current = self.head
    if current is None:
      return None
    max_node = current
    next_up = current.get_next()
    while next_up:
      if next_up.get_value() > max_node.get_value():
        max_node = next_up
      else:
        next_up = next_up.get_next()
    return max_node.get_value()



