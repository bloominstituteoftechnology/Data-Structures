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
    new_node=Node(value)
    if self.head == None:	
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node
    return self

    
  def remove_head(self):
    #check if there is no head
    if not self.head:
      return None
    #if head has no next, then there is only one element
    if not self.head.next_node:
      #store a reference to the current head
      head=self.head
      #delete the head reference
      self.head=None
      #point the tail to None
      self.tail=None
      return head.value
    else:
      #the list has more than 1 element
      value=self.head.value
      self.head=self.head.next_node
      return value
      

  def contains(self):
    pass

  def get_max(self):
    pass
