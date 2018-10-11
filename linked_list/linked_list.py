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
    new_node = Node(value, None)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    elif self.tail != None:
      self.tail.set_next(new_node)
      self.tail = new_node

  def remove_head(self):
    if self.head == None:
      return None
    else:
      removed_node = self.head.value
      if self.head.get_next() == None:
        self.head = None
        self.tail = None
        return removed_node
      else:
        self.head = self.head.get_next()
        return removed_node

  def contains(self, value):
    current = self.head
    if current == None:
      return False
    else:
      while current != None:
        if current.value == value:
          return True
        current = current.get_next()
      return False

  def get_max(self):
    if self.head == None:
      return None
    else:
      max_value = self.head.value
      current = self.head
      while current != None:
        if current.value > max_value:
          max_value = current.value
        current = current.get_next()
    return max_value
