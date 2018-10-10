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
    if self.tail is None:
      first_node = Node(value)
      self.head = first_node
      self.tail = first_node
    else:
      newest_node = Node(value)
      self.tail.next_node = newest_node
      self.tail = newest_node
      self.tail.next_node = None

  def remove_head(self):
    if self.head:
      removed = self.head
      self.head = self.head.next_node
      return removed.value

  def contains(self, value):
    if self.head:
      search_node = self.head
      while search_node is not None:
        if search_node.value == value:
          return True
        search_node = search_node.next_node
      return False
    

  def get_max(self):
    pass
