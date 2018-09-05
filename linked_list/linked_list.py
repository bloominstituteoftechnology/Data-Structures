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
    # Check if first node
    if not self.head:
      self.head = self.tail = Node(value, None)
    else:
      newNode = Node(value, None)
      self.tail.set_next(newNode)
      self.tail = newNode

  def remove_head(self):
    # Check if no items
    if not self.head:
      return None
    else:
      # Check if only one item in list, and unlink tail
      if self.head == self.tail:
        self.tail = None
      kill_node = self.head
      self.head = self.head.get_next()
      return kill_node.get_value()

  def contains(self, value):
    node = self.head
    while node is not None:
      if node.get_value() == value:
        return True
      else:
        node = node.get_next()
    return False

  def get_max(self):
    # Check if no nodes
    if not self.head:
      return None
    max_val = self.head.get_value()
    node = self.head
    while node is not None:
      if node.get_value() > max_val:
        max_val = node.get_value()
      node = node.get_next()
    return max_val
