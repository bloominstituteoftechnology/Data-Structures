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
    # Check to see if the list has a head
    if not self.head: 
      self.head = new_node 
      # Don't forget the tail 
      self.tail = new_node 
    else: 
      # We have a non-empty list 
      # Setting the last node's 'next' to the new node 
      self.tail.next_node = new_node
      # Update the linked list's 'tail' reference 
      self.tail = new_node 

  def remove_head(self):
    # first check if there is no head 
    if not self.head: 
      return None
    if not self.head.next_node: 
      head = self.head 
      self.head = None 
      self.tail = None 
      return head. value 
    else: 
      value = self.head.value
      self.head = self.head.next_node
      return value 

  def contains(self, value):
    if not self.head: 
      return None
    current = self.head
    while current: 
      if current.value == value: 
        return True
      current = current.next_node
    return False 

  def get_max(self):
    if not self.head: 
      return None 
    max_value = self.head.value 
    current = self.head.get_next() 
    while current: 
      if max_value < current.value: 
        max_value = current.value 
      current = current.next_node
    return max_value

a = LinkedList()
a.add_to_tail(1)
a.add_to_tail(2)
a.add_to_tail(3)
a.add_to_tail(4)
a.add_to_tail(5)
a.add_to_tail(6)
a.add_to_tail(7)
a.add_to_tail(8)
a.add_to_tail(9)
a.add_to_tail(10)
a.add_to_tail(11)
a.add_to_tail(12)

