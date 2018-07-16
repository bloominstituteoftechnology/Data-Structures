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
    nn = Node(value)
    if self.tail == None:
      if self.head == None:
        self.head = nn
      else:
        self.head.next_node = nn
    else:
      self.tail.next_node = nn
      
    self.tail = nn

  def remove_head(self):
    #print("shv", self.head.value)
    if self.head != None:
      prev_head = self.head
      self.head = self.head.next_node
      return prev_head.value
    return None
    

  def contains(self, value):
    current = self.head
    found = False
    while current is not None and not found:
        if current.get_value() == value:
            found = True
        else:
            current = current.get_next()

    return found

  def get_max(self):
    if self.head == None:
      return None
    largest = self.head.value
    current = self.head
    while current != None:
      if current.value > largest:
        largest = current.value
      current = current.next_node
    return largest
