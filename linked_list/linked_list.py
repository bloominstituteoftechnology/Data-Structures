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

  # add an itme to the end of the list
  def add_to_tail(self, value):
    # if value is a proper node then turn it into one
    if not isinstance(value, Node):
      value = Node(value)

    # if it is an empty list, then add value as head of the list
    if self.head is None:
      self.head = value

    else:
      # if it is not a empty list, then add value as the tail of the list
      self.tail.next = value

    self.tail = value

    return

  def remove_head(self):
    pass

  def contains(self, value):
    pass

  def get_max(self):
    pass
