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
    if not self.head and not self.tail:
        self.head = node
        self.tail = node
    elif self.head == self.tail:
        self.head.next = node
        self.tail = node
    else:
        self.tail.next = node
        self.tail = node

  def remove_head(self):
    pass

  def contains(self):
    pass

  def get_max(self):
    pass
