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
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      self.tail.set_next(node)
      self.tail = self.tail.get_next()

  def remove_head(self):
    if self.head != None:
      headVal = self.head.value
      if self.head.next_node != None:
        self.head = self.head.next_node
      else:
        self.head = None
        self.tail = None

      return headVal

  def contains(self, value):
    if self.head == None:
      return False
    node = self.head
    while True:
      if node.get_value() == value:
        return True
      if node.next_node == None:
        return False
      node = node.get_next()

  def get_max(self):
    pass
  
  def print_values(self):
    node = self.head
    print(node.get_value())
    while True:
      node = node.get_next()
      print(node.get_value())
      if(node.get_next() == None):
        break

