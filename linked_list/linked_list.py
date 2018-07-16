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
    if self.tail is None:
      self.tail = Node(value)
      self.head = self.tail
    else:
      self.tail.next_node = Node(value)
      self.tail = self.tail.next_node 

  def remove_head(self):
    if self.head == None:
      return None
    else:
      temp = self.head.value
      self.head = self.head.next_node
      return temp

  def contains(self, value):
    current = self.head
    while current is not None:
      if current.value == value:
        return True
      else:
        current = current.next_node
    return False

  def get_max(self):
    if self.head == None:
      return None
    maximum = self.head.value
    current = self.head
    while current is not None:
      if current.value > maximum:
        maximum = current.value
      current = current.next_node
    return maximum
