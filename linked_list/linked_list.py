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
    if self.head is None:
      self.head = value
    else:
      runner = self.head
      while runner.get_next():
        runner = runner.next
        runner.next = value
        self.tail = value
    pass

  def remove_head(self, value):
    if self.head is None:
      self.head = value
    else:
      value.set_next(self.head)
      self.head = value
    pass  

  def contains(self, value):
    if self.head is None:
      print ("self.head is None")
      return False
    else:
      print ("in runner...")
      runner = self.head
      while runner.get_next():
        print (value)
        if runner.value == value:
          return True
      return False
    pass

  def get_max(self):
    pass
