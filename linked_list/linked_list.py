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

  def remove_head(self):
    if self.head == None:
      return None
    elif self.head.next_node == None:
      removed_head = self.head.get_value()
      self.head = None
      self.tail = None
      return removed_head
    else:
      removed_head = self.head.get_value()
      self.head = self.head.next_node
      return removed_head

  def contains(self, value):
    pass

  def get_max(self):
    pass
