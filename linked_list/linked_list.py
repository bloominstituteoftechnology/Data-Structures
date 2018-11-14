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
    if not self.head:
      self.head = Node(value)
      self.tail = self.head
      return
    else:
      if self.head == self.tail:
        print ('this happened once')
        self.head.set_next(Node(value))
      else:
        self.tail.set_next(Node(value))
    self.tail = Node(value)

  def remove_head(self):
    if self.head:
      new_head = self.head.get_next()
      self.head = new_head

  def contains(self, value):
    node_checked = self.head
    while node_checked != None:
      if node_checked.get_value() == value:
        return True
      else:
        node_checked = node_checked.get_next()
    return False


  def get_max(self):
    pass
