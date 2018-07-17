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
    newNode = Node(value)
    if self.head == None:
        self.head = newNode
    else:
        self.tail.set_next(newNode)
    self.tail = newNode

  def remove_head(self):
    aux = self.head
    if aux != None:
      self.head = aux.get_next()
      if self.head == None:
        self.tail = None
      return aux.get_value()
    return None

  def contains(self, value):
    node = self.head
    while node != None:
      if node.get_value() == value:
        return True
      node = node.get_next()
    return False

  def get_max(self):
    if self.head == None:
      return None
    max = self.head.get_value()
    node = self.head
    while node != None:
      if node.get_value() > max:
        max = node.get_value()
      node = node.get_next()
    return max
