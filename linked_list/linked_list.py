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
    if self.tail is not None:
      self.tail.set_next(node)
    else:
      self.head = node
    self.tail = node

  def remove_head(self):
    if self.head is not None:
      val = self.head.value
      newHead = self.head.next_node
      if newHead is None:
        self.tail = None
      else: 
        self.tail = newHead.next_node
      self.head = newHead
      return val
    else: 
      return None
      # We never set tail to something that isn't none

      
  def contains(self, value):
    if self.head is not None:
      curr_node = self.head
      while True:
        if curr_node is None:
          return False
        elif curr_node.value == value:
          return True
        else:
          curr_node = curr_node.get_next()

  def get_max(self):
    if self.head is not None:
      curr_node = self.head
      max = float("-inf")
      while curr_node is not None:
        if curr_node.value > max and curr_node is not None:
          max = curr_node.value
        else:
          curr_node = curr_node.get_next()
      return max
