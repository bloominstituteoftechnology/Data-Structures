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
    NewNode = Node(value)
    if self.head == None:
      self.head = NewNode
      self.tail = self.head
    else:
      self.tail.set_next(NewNode)
      self.tail = NewNode
  
  def remove_head(self):
    if self.head:
      del_head = self.head
      self.head = self.head.get_next()
      self.tail = None
      return del_head.value

  def contains(self, value):
    currentNode = self.head
    contains = False
    while currentNode and contains == False:
      if currentNode.value == value:
        contains = True
      else:
        currentNode = currentNode.get_next()
    return contains

  def get_max(self):
    maxValue = 0
    currentValue = self.head
    if currentValue is None:
      return None
    while currentValue:
      if currentValue.get_value() > maxValue:
        maxValue = currentValue.get_value()
      currentValue = currentValue.get_next()
    return maxValue
