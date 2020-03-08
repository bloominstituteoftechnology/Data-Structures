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
    if not self.head:
      self.head = node
      self.tail = node
    else:
      self.tail.set_next(node)
      self.tail = node
    

  def remove_head(self):
    curr_node = self.head
    if not self.head:
      return None
    if not self.head.get_next():
      x = self.head
      self.head = None
      self.tail = None
      return x.get_value()
    cur_value = self.head.get_value()
    self.head = self.head.get_next()
    return cur_value
    

  def contains(self, value):
    curr_node = self.head
    while True:
      if not curr_node:
        return False
      elif curr_node.value == value:
        return True
      else:
        curr_node = curr_node.get_next()
    

  def get_max(self):
    if not self.head:
      return None
    curr_node = self.head.get_next()
    max_node = self.head
    while curr_node:
      if curr_node.get_value() > max_node.get_value():
        max_node = curr_node
      else:
        curr_node = curr_node.get_next()

    return max_node.get_value()
    
