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
      self.tail = newNode
    else:
      self.tail.set_next(newNode)
      self.tail = newNode

  def remove_head(self):
    if self.head != None:
      nodeToDelete = self.head.get_value()
      self.head = self.head.get_next()
      self.tail = None
      return nodeToDelete

  def contains(self, value):
    index = self.head
    while index != None:
      if index.get_value() == value:
        return True
      else:
        index = index.get_next()

  def get_max(self):
    index = self.head
    if index == None:
      return None
    else:    
      maxValue = 0
      currentValue = 0
      while index != None:
        currentValue = index.get_value()
        if currentValue >= maxValue:
          maxValue = currentValue
          # index = index.get_next()
        index = index.get_next()        
        # elif currentValue < maxValue:
        #   index = index.get_next()
        # else:
        #   index = None
      return maxValue