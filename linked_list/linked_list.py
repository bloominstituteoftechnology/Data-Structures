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
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node

  def remove_head(self):
    if self.head is None:
      return None
    elif self.head.get_next():
      temp = self.head.get_value()
      self.head = self.head.get_next()
      return temp
    else:
      temp = self.head
      self.head = None
      self.tail = None
      return temp.value

  def contains(self, value):
    current_node = self.head
    if current_node != None:
      while current_node != None:
        if current_node.get_value() == value:
          return current_node.get_value()
        else:
          current_node = current_node.get_next()

  def get_max(self):
    current_node = self.head
    max_value = 0
    if current_node != None:
      while current_node != None:
        temp_value = current_node.get_value()
        if temp_value > max_value  :
          max_value = temp_value
        else:
          current_node = current_node.get_next()
      return max_value
