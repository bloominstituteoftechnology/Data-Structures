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
      self.tail = None
    else:
      self.tail.set_next(newNode)
      self.tail = newNode

  def remove_head(self, value):
    self.head.value = self.head.next_node
    self.head.set_next(self.head.next_node)
    # if self.head is None:
    #   self.head = value
    # else:
    #   value.set_next(self.head)
    #   self.head = value

  def contains(self, value):
    if self.head == None:
      return False
    else:
      runner = self.head
      while runner:
        if runner.get_value():
          return True
        runner = runner.get_next()
      return False

  def get_max(self):
    if self.head == None:
      return None
      max = self.head.get_next()
      current = self.head.get_next
    while current:
      begin = current.get_value()
    if begin > max:
      current = current.get_next()
        return max
    pass
