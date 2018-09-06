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
    if not self.head:
      self.head = node
      self.tail = node
    else:
      self.tail.set_next(node)
      self.tail = node

  def remove_head(self):
    if self.head:
      head = self.head
      self.head = self.head.get_next()
      self.tail = None
      return head.value

  def contains(self, value):
    current_node = self.head
    while current_node:
      if current_node.value == value:
        return True
      current_node = current_node.get_next()
    return False

  def get_max(self):
    current_node = self.head
    if not current_node:
      return None

    current_value = current_node.value

    while current_node:
      if current_node.value > current_value:
        current_value = current_node.value

      current_node = current_node.get_next()

    return current_value
