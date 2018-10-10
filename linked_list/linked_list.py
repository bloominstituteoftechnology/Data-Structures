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
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node

  def remove_head(self):
    if self.head != None:
      if self.head.next_node != None:
        prev_head = self.head
        self.head = self.head.next_node
        return prev_head.value
      else:
        prev_head = self.head
        self.head = None
        self.tail = None
        return prev_head.value
    
  def contains(self, value):
    if self.head == None:
      return False
    else:
      h = self.head
      while h:
        if h.value == value:
          return True
        h = h.get_next()
      return False

  def get_max(self):
    if self.head == None:
      return None
    else:
      max_value = self.head.value
      if self.head.next_node != None:
        h = self.head
        while h.next_node != None:
          if h.next_node.value > max_value:
            max_value = h.next_node.value
          h = h.get_next()
      return max_value

