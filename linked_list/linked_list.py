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
    new_node = Node(value, None)

    if self.head == None:
      self.head = new_node

    if self.tail == None:
      self.tail = new_node
    elif self.tail != None:
      self.tail.next_node = new_node
      self.tail = new_node

  def remove_head(self):
    if self.head == None:
      return None
    else:
      print(self.head.value,self.head.next_node)
      removed_node = self.head.value
      self.head = self.head.next_node
      return removed_node

  def contains(self, value):
    if self.head == None:
      return None
    else:
      while self.head.next_node != None:
        if self.head.next_node.value == value:
          return True
        else:
          return False

  def get_max(self):
    max_value = 0
    if self.head == None:
      return None
    else:
      while self.head.next_node != None:
        if self.head.next_node.value > self.head.value:
          max_value = self.head.next_node.value
    return max_value
