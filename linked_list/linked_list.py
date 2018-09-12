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
    self.size = 0

  def add_to_tail(self, value):
    if self.tail:
      self.tail.set_next(Node(value))
      self.tail = self.tail.get_next()
    else:
      self.tail = Node(value)
      self.head = self.tail
    
    self.size += 1

  def remove_head(self):
    if self.head:
      old_head = self.head.get_value()
      self.head = self.head.get_next()
      self.size -= 1

      if not self.head or not self.head.get_next():
        self.tail = self.head
      return old_head
    return None  

  def contains(self, value):
    curr = self.head
    while curr:
      if curr.get_value() == value:
        return True
      curr = curr.get_next()
    return False    

  def get_max(self):
    if self.head:
      curr = self.head
      curr_max = curr.get_value()
      while curr:
        if curr.get_value() > curr_max:
          curr_max = curr.get_value()
        curr = curr.get_next()
      return curr_max
    return None    
