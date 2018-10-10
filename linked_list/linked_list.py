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
  
  def get_length(self):
    count = 0
    counter = self.head
    while counter:
      count += 1
      counter = counter.get_next()
    return count    

  def add_to_tail(self, value):
    # self.tail.next_node = self.tail
    # self.tail = Node(value)

    self.tail = Node(value)
    if self.head is None:
      self.head = Node(value)
      return
    lastNode = self.head
    while(lastNode.next_node):
      lastNode = lastNode.next_node
    lastNode.next_node = Node(value)

  def remove_head(self):
    original_head = self.head
    x = original_head
    
    self.head = self.head.get_next()
    original_head = None

    return x.get_value()

  def contains(self, value):
    search = self.head
    while search:
      if search.get_value() == value:
        return True
      search = search.get_next()
    return False

  def get_max(self):
    if self.head == None:
      return None

    maxElement = int(self.head.value)
    search = self.head
    while search: 
      if search.get_value() > maxElement:
        maxElement = search.get_value()
      search = search.get_next()
    return maxElement

