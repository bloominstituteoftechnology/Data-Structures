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
      self.tail = self.head = Node(value)
      return

    new_node = Node(value)
    self.tail.next_node = new_node
    self.tail = new_node

  def remove_head(self):
    if self.head is None:
      return None

    old_head = self.head
    self.head = self.head.next_node
    old_head.next_node = None
    if self.head is None:
      self.tail = None

    return old_head.value

  def contains(self, value):
    cur = self.head
    while cur is not None:
      if cur.value == value:
        return True
      cur = cur.next_node
    return False

  def get_max(self):
    if self.head is None:
      return None

    cur = self.head
    max_val = cur.value
    while cur is not None:
      max_val = max(cur.value, max_val)
      cur = cur.next_node
    return max_val