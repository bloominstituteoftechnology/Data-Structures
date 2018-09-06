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
    newNode = Node(value)
    if not self.head:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next_node = newNode
      self.tail = newNode

  def remove_head(self):
    if not self.head:
      return None
    if not self.head.next_node:
      value = self.head.value
      head = self.head
      self.head = None
      self.tail = None
      return head.value
    else:
      value = self.head.value
      self.head = self.head.next_node
      return value

  def contains(self, value):
    if not self.head:
      return None
    currentNode = self.head
    while currentNode:
      if currentNode.value == value:
        return True
      currentNode = currentNode.get_next()
    return False

  def get_max(self):
    if not self.head:
      return None
    value = self.head.value
    max_value = self.head.value
    currentNode = self.head.get_next()
    while currentNode:
      if currentNode.value > max_value:
        max_value = currentNode.value
      currentNode = currentNode.next_node
    return max_value
