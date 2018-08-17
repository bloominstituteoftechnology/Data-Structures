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
    if self.tail == None:
      if self.head == None:
        self.head = new_node
      else:
        self.head.next_node = new_node
    else:
      self.tail.next_node = new_node
    self.tail = new_node

  def remove_head(self):
    if self.head != None:
      old_head = self.head
      self.head = self.head.next_node
      if self.head == None:
        self.tail = None
      return old_head.value
    return None

  def contains(self, value):
    curr = self.head
    while curr != None:
      if curr.value == value:
        return True
      curr = curr.next_node
    return False

  def get_max(self):
    if self.head == None:
      return None
    biggest = self.head.value
    curr = self.head
    while curr != None:
      if curr.value > biggest:
        biggest = curr.value
      curr = curr.next_node
    return biggest
