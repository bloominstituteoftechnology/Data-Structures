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
      self.tail.set_next(new_node)
      self.tail = new_node

  def remove_head(self):
    if self.head == None:
      return None
    else:
      removed_head = self.head.get_value()
      self.head = self.head.get_next()
      self.tail = None
      return removed_head

  def contains(self, value):
    current_node = self.head
    while current_node:
      if current_node.get_value() == value:
        return True
      else:
        current_node = current_node.get_next()
    return False


  def get_max(self):
    pass
