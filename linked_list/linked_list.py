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
    if self.tail == None:
      if self.head == None:
        self.tail = node
      else:
        self.head.next_node = node
    else:
      self.tail.next_node = node
    self.tail = node
    

  def remove_head(self):
    if self.head != None:
      head = self.head
      self.head = self.head.next_node
      return head.value
    else:
      return None

  def contains(self, value):
    curr = self.head
    while curr:
      if curr.get_value() == value:
        return True
          curr = curr.get_next()
    return False

  def get_max(self):
    if self.head is None:
      return None
    max_value = self.head.get_value()
    curr = self.head 
    while curr:
      if curr.get_value() > max_value:
        max_value = curr.get_value()
      curr = curr.get_next()
    return max_value
