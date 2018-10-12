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
    newNode = Node(value, None)
    if self.tail:
        self.tail.set_next(newNode)
    if not self.head:
        self.head = newNode
    self.tail = newNode

  def remove_head(self):
    if not self.head:
        return None
    prevhead = self.head.get_value()
    self.head = self.head.get_next()
    if not self.head:
        self.tail = None
    return prevhead

  def contains(self, value):
    node = self.head
    while node:
        if node.get_value() == value:
            return True
        node = node.get_next()
    return False

  def get_max(self):
    node = self.head
    max = None
    while node:
        if not max:
            max = node.get_value()
        elif node.get_value() > max:
            max = node.get_value()
        node = node.get_next()
    return max
