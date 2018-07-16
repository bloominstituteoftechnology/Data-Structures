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
    new_value = Node(value)
    if self.tail == None: 
      try:
        self.head = new_value
      except:
        self.head.next_node = new_value
    else:
      self.tail.next_node = new_value
    
    self.tail = new_value

  def remove_head(self):
    pass

  def contains(self):
    pass

  def get_max(self):
    pass
