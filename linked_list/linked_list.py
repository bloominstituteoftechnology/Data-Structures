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
    new_node = Node(value) 
    if self.head == None:
      self.head = new_node
    else:
      self.tail.next_node = new_node
    self.tail = new_node

  def remove_head(self):
    if self.head == None:
      return None 
    elif self.head.next_node == None:
      node = self.head
      self.head = None
      self.tail = None
      return node.value
    else:
      node = self.head
      self.head = self.head.next_node
      node.next_mode = None
      return node.value
    current_node = self.head
    self.head = self.head.next_node
    return current_node.value

  def contains(self, value):
    result = self.head
    while result is not None:
      if result.get_value() == value:
        return True
      else:
        result = result.get_next()
    return False


  def get_max(self):
    maxNode = None
    current = self.head
    if current is not None:
      maxNode = current.get_value()
    while current is not None:
      if current.get_value() > maxNode or maxNode is None:
        maxNode = current.get_value()
      current = current.get_next()
    return maxNode
