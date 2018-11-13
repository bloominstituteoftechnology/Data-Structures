"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node
  def __str__(self):
    return str(f'Node Object value: {self.value}, next_node: {self.next_node}')

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
  def __str__(self): 
    return str(f'\n(self.head: {self.head}) (self.tail: {self.tail})\n')

  def add_to_tail(self, value):

    if self.head == None and self.tail == None:
      self.head = Node(value)
      self.tail = Node(value)
    else:
      if self.head.value == None and self.tail.value == None:
        self.head = Node(value)
        self.tail = Node(value)
      else:
        if self.head.next_node == None:
          self.head.set_next(value)
        self.tail = Node(value)


  def remove_head(self):

    # print('in def remove_head')
    # print(self)

    if self.head == None and self.tail == None:
      return None

    if self.head.next_node != None:
      return_val = self.head.value
      self.head = Node(self.head.next_node)
      self.tail = Node(self.head.value)
      # print(self)
      return return_val
    else:
      return_val = self.head.value
      self.head = None
      self.tail = None
      # print(self)
      return return_val

  def contains(self, value):
    # print('in contains')
    # print(self)
    if self.head == None and self.tail == None:
      pass
    else:
      if self.head.value == value or self.head.next_node == value or self.tail.value == value:
        return True
      else:
        return False

  def get_max(self):
    # print(self)
    if self.head == None:
      pass
    else:
      if self.head.value > self.tail.value:
        return self.head.value
      else:
        return self.tail.value