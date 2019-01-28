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
    new_tail = Node(value)
    if self.tail is not None:
      self.tail.set_next(new_tail)
    else:
      self.head = new_tail
    self.tail = new_tail

  def remove_head(self):
    if self.head is not None:
      cur_head = self.head.get_value()
      new_head = self.head.get_next()
      if new_head is not None:
        self.head = new_head
      else:
        self.tail = None
        self.head = None
      return cur_head
    

  def contains(self, value):
    pass

  def get_max(self):
    pass
