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
    self.max = None

  def add_to_tail(self, value):
    node = Node(value)
    self.max = value if not self.max or value > self.max else self.max

    if not self.head:
        self.head = node
        self.tail = node
    else:
        self.tail.next_node = node
        self.tail = node

  def remove_head(self):
    head = None if not self.head else self.head.get_value()
    if self.head == self.tail:
        self.head = None
        self.tail = None
    else:
        self.head = self.head.next_node
    return head

  def contains(self, value):
    current_node = self.head
    while current_node:
        if current_node.get_value() == value:
            return True
        current_node = current_node.next_node
    return False

  def get_max(self):
    return self.max
