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
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
    else:
      new_tail = Node(value)
      self.tail.set_next(new_tail)
      self.tail = new_tail

  def remove_head(self):
    if self.head == None:
      return None
    else:
      if self.head == self.tail:
        self.tail = None
      old_head = self.head
      self.head = self.head.get_next()
      return old_head.get_value()

  def contains(self, value):
    current_node = self.head
    if self.head == None:
      return False
    while not current_node == None:
      print(current_node.get_value())
      if value == current_node.get_value():
        return True
      current_node = current_node.get_next()
    return False    

  def get_max(self):
    current_max = 0
    current_node = self.head
    if self.head == None:
      return None
    while not current_node == None:
      if current_node.get_value() > current_max:
        current_max = current_node.get_value()
      current_node = current_node.get_next()
    return current_max
