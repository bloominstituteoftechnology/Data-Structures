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
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail = new_node
      self.head.set_next(self.tail)
      self.tail.set_next(None)

  def remove_head(self):
    after_head = self.head.next_node
    curr_head = self.head
    if self.head:
      self.head = None
      return after_head

  def contains(self, value):
    test_node = self.head
    while test_node is not None:
      if test_node.value == value:
        return True
      test_node = test_node.get_next()
    return False

  def get_max(self):
    pass
