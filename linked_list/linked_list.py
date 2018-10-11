"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
import math

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
    else:
      self.tail.set_next(new_node)
    self.tail = new_node
 
  def remove_head(self):
    #define the current head
    current = self.head

    if self.head is not None:
      removed = self.head.get_value()
      current = self.head.get_next()
      self.head = current

    elif self.head.next_node == None:
      removed = self.head.get_value()
      self.head = None
      self.tail = None

    elif self.head == None:
      return None
    
    return removed


  def contains(self, value):
    current = self.head
    found = False
    while current and found is False:
      if current.get_value() == value:
        found = True
      else:
        current = current.get_next()
    if current is None:
      return None
    return current

  def get_max(self):
    if self.head == None or self.tail == None:
      return None
    current = self.head
    max_val = -math.inf

    while current.next_node != None:
      if current.get_value() > max_val:
        max_val = current.get_value()
      current = current.get_next()

    if self.tail.get_value() > max_val:
      max_val = self.tail.get_value()
    
    return max_val