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
    
    if self.head is None:
      self.head = new_node
      self.tail = new_node
      return
    
    last = self.head
    
    while last.next_node:
      last = last.next_node
    
    last.next_node = new_node
    self.tail = last.next_node

  def remove_head(self):
    if self.head is None:
      return None
      
    removeNode = self.head.value
    self.head = self.head.next_node
    return removeNode

  def contains(self, value):
    last = self.head
    
    while last:
      if last.value == value:
        return True
      last = last.next_node
      
    return False

  def get_max(self):
    last = self.head
    maxV = None
    
    while last:
      if maxV is None:
        maxV = last.value
      else:
        maxV = max(last.value, maxV)
      last = last.next_node
      
    return maxV
    
    
