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
    # Empty linkedlist 
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
    # Linkedlist one node 
    elif self.head.next_node == None:
      self.head.next_node = Node(value)
      self.tail = self.head.next_node
    else:
      self.tail.next_node = Node(value)
      self.tail = self.tail.next_node

  def remove_head(self):
    # Empty linkedlist
    if self.head == None:
      return None
    # Linkedlist one node
    elif self.head.next_node == None:
      removed_value = self.head.value
      self.tail = None
      self.head = None
      return removed_value
    elif self.head:
      removed_value = self.head.value
      self.head = self.head.next_node
      return removed_value

  def contains(self, value):
    current_node = self.head
    while current_node:
      if current_node.value == value:
        return True
      current_node = current_node.next_node
    
  def get_max(self):
    if self.head == None:
      return None
    current_node = self.head
    max_value = self.head.value
    while current_node:
      if current_node.value > max_value:
        max_value = current_node.value
      current_node = current_node.next_node
    return max_value