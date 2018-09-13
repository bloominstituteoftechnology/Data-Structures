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
    tail = Node(value)
    if not self.head:
      self.head = tail
    else:
      self.tail.set_next(tail)
    
    self.tail = tail

  def remove_head(self):
    if self.head == None: 
      return None
    else:
      current = self.head
      self.head = current.get_next()
      self.tail = None
      return current.value

  def contains(self, value):
    if not self.head:
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
