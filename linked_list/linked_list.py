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
      self.tail = node

  def remove_head(self):
    if self.head == None:
      return self.head

    else:
      temp = self.head.get_value()
      self.head = self.head.get_next()
      if self.head == None:
        self.tail = None
      return temp

  def contains(self, value):
    current = self.head

    if self.head is None:
      return False

    else:
      while current != None:
        if current.get_value() == value:
          return True

        elif current is None:
          return False

        else:
          current = current.get_next()

  def get_max(self):
    max_value = 0
    current = self.head
    
    if current == None:
      self.tail = None
      return None
      
    else:
      while current != None:
        if current.get_value() > max_value:
          max_value = current.get_value()
        else:
          current = current.get_next()

    return max_value
