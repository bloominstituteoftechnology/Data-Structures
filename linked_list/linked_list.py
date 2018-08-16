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
    else:
      self.tail.set_next(new_node)
      self.tail = new_node
    return new_node


  def remove_head(self):
    if self.head == None: return None
    removed_head = self.head.get_value()
    self.head = self.head.get_next()
    return removed_head

  def contains(self, value):
    current_node = self.head
  
    if current_node == None: return False
    if current_node.get_value() == value: return True

    while current_node.get_next() != None:
      current_node = current_node.get_next()
      if current_node.get_value() == value: return True

    return False

  def get_max(self):
    current_node = self.head

    if current_node == None: return None
    current_max = self.head.get_value()

    while current_node.get_next() != None:
      current_node = current_node.get_next()
      current_value = current_node.get_value()
      if current_max < current_value: current_max = current_value

    return current_max
