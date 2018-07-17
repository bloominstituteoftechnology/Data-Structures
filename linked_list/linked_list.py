from .linked_list import LinkedList
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
    if self.head == None:
      # let's make a tail
      self.head = new_node
    if self.tail != None:
      self.tail.next_node(new_node)
      self.tail = new_node

  def remove_head(self):
    #update the head to be formre second node of the linked list
    #self.head = self.head.next_node
    if self.head == None: return None
    remove_value = self.head.value
    new_head = self.head.next_node
    self.head = new_head
    return removed_value
    
  def contains(self, target):
    #if input value exists in the list, return True
    #if not, return False
    current_node = self.head

    if current_node == None: return False
    if current_node.value == target: returm True

    while current_node.next_node: != None:
      # stuff
      next_node = current_node.next_node
      current_node = next_node
      if current_node.value == target: return True

    return False

  def get_max(self):
    pass
