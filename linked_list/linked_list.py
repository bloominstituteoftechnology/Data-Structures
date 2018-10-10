import math 
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
    """Create a new node 
       Assign it's next reference to None
       Set the next reference of the tail to point to this new node.
       then update the tail reference itself to this new node. 
       error messages will occur without an inital check for the head and tail
       if the head and tail is none that means the linkedlist is empyt so the first item has to be both the head and the tail. 
    """
    new_node = Node(value) 
    new_node.set_next(None)
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node
    

  def remove_head(self):
    """
    set the head to the next node 
    error messages will occur without an inital check for the head. 
    """
    if self.head is not None:
      next_in_line = self.head.get_next()
      self.head = next_in_line 
    else:
      print("There is no head")

  def contains(self, value):
    current = self.head 
    while True:
      if value == current.get_value():
        print ("Its in here")
        return True 
      current = current.get_next()
      if current is None:
        return False 
        break 

  def get_max(self):
    max_value = math.inf * -1
    current = self.head
    while True: 
      if current.get_value() > max_value:
        max_value = current.get_value()
      current = current.get_next()
      if current is None:
        return max_value