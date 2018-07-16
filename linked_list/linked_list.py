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
    new_node = Node(value)

    if self.tail == None: 
      try:
        self.head = new_node
      except:
        self.head.next_node = new_node
    else:
      self.tail.next_node = new_node
    
    self.tail = new_node

  def remove_head(self):
    if self.head != None:
      try:
        self.head = self.head.next_node
      except:
        self.head = None
    else:
      return None

  def contains(self, value):
    contain = False
    pointer = self.head
    
    while pointer != None:
      if pointer == value:
        contain = True
      pointer = pointer.next_node

    return contain

  def get_max(self):
    pass
