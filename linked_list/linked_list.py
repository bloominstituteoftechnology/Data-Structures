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
    if self.head is None:      
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.set_next(newNode)
      self.tail = newNode

    pass

  def remove_head(self):
    if self.head is None:
      return None
    else:
      value = self.head.get_value()
      if self.head is self.tail:
        self.tail = self.head.get_next()
      self.head = self.head.get_next()
      return value

    pass

  def contains(self, value):
    if self.head is None:
      return None

    node = self.head
    while True:
      if node.value is value:
        return True
      if node.get_next() is None:
        return False
      else:
        node = node.get_next()

  def get_max(self):
    node = self.head
    if node is None:
      return None

    value = node.get_value()    
    while node.get_next() is not None:
      node= node.get_next()
      if node.get_value() > value:
        value = node.get_value()
      
    
    return value
      