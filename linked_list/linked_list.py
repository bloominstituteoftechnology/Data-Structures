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
    new_node.set_next(self.tail)
    self.tail = new_node

  def remove_head(self):
    #define the current head
    current = self.head
    removed = None
    #set the next node as the new head
    if current is None:
      raise ValueError("Nothing to remove")
    else:
      removed.set_next(current.get_next())

  def contains(self, value):
    current = self.head
    found = False
    while current and found is False:
      if current.get_value() == value:
        found = True
      else:
        current = current.get_next()
    if current is None:
      raise ValueError("List does not contain value")
    return current

  def get_max(self):
    current = self.head
    return max(current.get_value(), current.get_next())
    
