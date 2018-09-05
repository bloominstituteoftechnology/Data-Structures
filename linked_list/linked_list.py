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
    val = Node(value)
    if self.head == None: 
        self.head = val
        self.tail = val
    else:
      self.tail.set_next(val)
      self.tail = val
    return val

  def remove_head(self):
    if self.head == None:
      return None
    val = self.head.get_value()
    self.head = self.head.get_next()
    return val
  
  def contains(self, target):
    thisNode = self.head
    while True:
      if thisNode == None:
        return False
      elif target == thisNode.value:
        return True
      elif thisNode.next_node == None:
        return False
      else:
        thisNode = thisNode.next_node

  def get_max(self):
    if self.head == None:
      return None
    elif self.head == self.tail:
      return self.head.value
    else:
      maxVal = self.head.value
      current_node = self.head.next_node

      while True:
        if current_node.value > maxVal:
          maxVal = current_node.value
        if current_node.next_node == None:
          return maxVal
        else: current_node = current_node.next_node
