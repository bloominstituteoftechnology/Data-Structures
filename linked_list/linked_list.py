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
    if self.head != None:
      self.tail.set_next(node)
      self.tail = self.tail.get_next()
    else:
      self.head = node
      self.tail = node

  def remove_head(self):
    if self.head != None:
      headVal = self.head.get_value()
      if self.head.get_next() != None:
        self.head = self.head.get_next()
      else:
        self.head = None
        self.tail = None

      return headVal

  def contains(self, value):
    if self.head == None:
      return False
    node = self.head
    while node:
      if node.get_value() == value:
        return True
      if node.get_next() == None:
        return False
      node = node.get_next()

  def get_max(self):
    if self.head == None:
      return None
    node = self.head
    maxValue = node.get_value()
    while node.get_next() != None:
      node = node.get_next()
  
      if maxValue < node.get_value():
        maxValue = node.get_value()
    return maxValue
