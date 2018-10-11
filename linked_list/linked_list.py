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
      new_node = Node(value)
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = Node(value)
      self.tail = self.tail.next_node

  def remove_head(self):
    if self.head == None:
      return self.head
    else:
      temp = self.head.get_value()
      self.head = self.head.get_next()
      if self.head == None:
        self.tail = None
      return temp

  def contains(self, value):
    cur_node = self.head
    if self.head is None:
      return False
    else:
      while cur_node is not None:
        if cur_node.get_value() == value: # RETURNS TRUE IF CURRENT NODE IS EQUAL TO VALUE
          return True     
        else:
          cur_node = cur_node.get_next() # CURRENT NODE CHANGES TO THE NEXT ONE IF NOT EQUAL TO VALUE. 

  def get_max(self):
    max_value = 0
    cur_node = self.head
    if cur_node == None:
      self.tail = None
      return None
    else:
      while cur_node is not None:
        if cur_node.get_value() > max_value:
          max_value = cur_node.get_value()
        elif cur_node.get_value() < max_value:
          cur_node = cur_node.get_next()
    return max_value
