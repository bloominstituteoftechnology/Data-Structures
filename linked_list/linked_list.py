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
    if self.head == None:
      self.head = x
      self.tail = x
    if self.tail != None:
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
    if self.head.get_value() == value:
        return True
    
    y = self.head.get_next()
    
    while True:
      if y == None:
        return False
      if y.get_value() == value:
        return True
      if y.get_next() == None:
        return False
      y = y.get_next()
      
  def get_max(self):
    if self.head == None:
      return None
    max = self.head.get_value()
    y = self.head.get_next()

    while True:
      if y == None:
        return max
      temp = y.get_value()
      if temp > max:
        max = temp 
      y = y.get_next()
      if y == None:
        break
    
    return max
      