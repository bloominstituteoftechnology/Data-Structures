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

    if self.head:
      if not self.tail:
        self.head.next_node = newNode
        self.tail = newNode
      else: self.tail.next_node = newNode
      self.tail = newNode
    else:
      self.head = newNode
      self.tail = newNode

  def remove_head(self):
    retObj = self.head
    if self.head:
      if self.head.next_node: self.head = self.head.next_node
      else:
        if self.head == self.tail: self.tail = None
        self.head = None
    if not retObj: return None
    else: return retObj.value

  def contains(self, value):
    if self.head:
      if self.head.value == value: return True
      else:
        curObj = self.head
        while 1:
          if curObj.value == value: return True
          elif curObj.next_node:
            curObj = curObj.next_node
          else: return False

  def get_max(self):
    maxValue = 0
    if self.head: maxValue = self.head.value
    else: return None
    curObj = None
    if self.head.next_node: curObj = self.head.next_node
    else: return maxValue
    while 1:
      if curObj.value > maxValue: maxValue = curObj.value
      if curObj.next_node: curObj = curObj.next_node
      else: return maxValue