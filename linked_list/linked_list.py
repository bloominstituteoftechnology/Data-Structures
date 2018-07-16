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
    if self.head == None:
      self.head = node
    elif self.head == self.tail and self.head != None:
      self.head.set_next(node)  
    else:
      self.tail.set_next(node)
    self.tail = node

  def remove_head(self):
    if self.head != None:
        head_value = self.head.get_value()
        self.head = self.head.get_next()
        return head_value
    if self.head == None:
        return None

  def contains(self, value):
    if self.head != None:
      i = self.head
      while i.get_next() != None:
        if i.get_value() == value:
          return True
        else:
          i = i.get_next()
      if self.tail.get_value() == value:
        return True
      return False
    if self.head == None:
      return False

  def get_max(self):
    if self.head != None:
      i = self.head
      max_num = i.get_value()
      while i.get_next() != None:
        i = i.get_next()
        if i.get_value() > max_num:
          max_num = i.get_value()
      return max_num
    if self.head == None:
      return None
