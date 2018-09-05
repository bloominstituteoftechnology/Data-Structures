"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""

# Should have the methods: add_to_tail, remove_head, contains, and get_max.
# add_to_tail replaces the tail with a new value that is passed in.
# remove_head removes and returns the head node.
# contains should search through the linked list and return true if a matching value is found.
# get_max returns the maximum value in the linked list.
# The head property is a reference to the first node and the tail property is a reference to the last node. Build your nodes with objects.


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
    new_tail = Node(value)
    if self.head is None:
      self.head = new_tail
    else:
      self.tail.next_node = new_tail
    self.tail = new_tail

  def remove_head(self):
    if self.head is not None:
      old_head = self.head
      self.head = self.head.get_next()
      self.tail = None
      return old_head.value

  def contains(self, value):
    current = self.head
    while current is not None:
      if current.value == value:
        return True
      current = current.next_node
    return False

  def get_max(self):
    if self.head == None:
      return None
    max_value = self.head.value
    current = self.head
    while current is not None:
      if current.value > max_value:
        max_value = current.value
      current = current.next_node
    return max_value

