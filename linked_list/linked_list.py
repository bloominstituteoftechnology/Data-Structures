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
    node = Node(value, None)
    if self.tail is None and self.head is None:
      self.tail = node
      self.head = node
    elif self.tail is not None:
      self.tail.next_node = node
      self.tail = node

  def remove_head(self):
    if self.head is not None:
      head_to_remove = self.head.value
    if self.head.next_node is not None:
      self.head = self.head.next_node
    elif self.head.next_node is None:
      self.head = None
      self.tail = None
    return head_to_remove
    else:
      return None

  def contains(self, value):
    curr_node = self.head

    while True:
      if curr_node == None:
        return False
    elif curr_node.value == value:
      return True
    else:
      curr_node = curr_node.next_node

  def get_max(self):
    current_max = 0
    current_node = self.head

    while current_node is not None:
      if current_node.value > current_max:
        current_max = current_node.value
        current_node = current_node.next_node
    return current_max if current_max > 0 else None 
