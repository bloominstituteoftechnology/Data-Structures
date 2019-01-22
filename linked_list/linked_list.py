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

    if self.tail is None or self.head is None:
      self.head = node
    else:
      self.tail.set_next(node)

    self.tail = node
   
  def remove_head(self):
    if self.head is not None:
      previous = self.head.value
      self.head = self.head.get_next()

      if self.head is None:
        self.tail = None
        
      return previous
    else:
      return None
    

  def contains(self, value):
    current = self.head

    # check to match current value, one of three cases will arise
    while True:
      if current is None:
        return False
      elif current.get_value() == value:
        return True
      else:
        current = current.get_next()

  def get_max(self):
    if self.head is None:
      return None
    
    # set these values to the head so we can start checking from one place
    max = self.head
    current = self.head

    # if current is greater than max, it becomes the new max and cycles to the next node
    while True:
      if current is None:
        return max.get_value()
      elif current.get_value() > max.get_value():
        max = current

      current = current.get_next()