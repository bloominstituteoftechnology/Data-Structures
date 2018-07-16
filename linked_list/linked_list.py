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
    
    if self.head == None:
      self.head = new_node
      self.tail = new_node

    elif self.head == self.tail:
      self.tail = new_node
      self.head.next_node = new_node

    else:
      self.tail.next_node = new_node
      self.tail = new_node

  def remove_head(self):
    removed = self.head
    if self.head.next_node != None:
      self.head = self.head.next_node
    else:
      self.head = None
    if removed.value:
      return removed.value

  def contains(self, target):
    current_node = self.head
    
    while True:

      if current_node == None:
        return False
      
      elif target == current_node.value:
        return True
      
      elif current_node.next_node == None:
        return False

      else:
        current_node = current_node.next_node

  def get_max(self):
    pass
