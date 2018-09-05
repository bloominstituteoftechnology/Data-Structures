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
    tail = Node(value)
    if not self.head:
      self.head = tail
    else:
      self.tail.set_next(tail)
    
    self.tail = tail

  def remove_head(self):
    pass

  def contains(self, value):
    last = self.head
    
    def test(last):
      if last == True:
        if last.value == value:
          return True
        last = last.next_node
        test(last)
      else:
        return false

  def get_max(self):
    pass