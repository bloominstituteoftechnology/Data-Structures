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
    x = Node(value)
    if not self.head:
      self.head = x
      self.tail = x
    if self.tail:
      self.tail.set_next(x)
      self.tail = x
      self.tail.set_next(None)

  def remove_head(self):
    if self.head == None:
      return None
    x = self.head.get_value()
    self.head = self.head.get_next()
    return x

  def contains(self, value):
    if self.head == None:
        return False
    
    current = self.head
    while current:
      if current.get_value() == value:
        return True
      current = current.get_next()

    return False
      
  def get_max(self):
    if not self.head:
      return None
    max = self.head.get_value()
    current = self.head.get_next()

    while current:
      temp = current.get_value()
      if temp > max:
        max = temp 
      current = current.get_next()
    
    return max
      