"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list

Change for Pull Request
"""
import math

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

    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
    # self.tail.set_next(new_node)
    self.tail = new_node
    print('value added to tail', self.tail.get_value())

  def remove_head(self):
    """
    `remove_head` removes and returns the head node
    ---
    # placeholder for the next after head so we have access to it

    # self.head = None
    # self.head = placeholder
    self.head = self.head.get_next  
    """
    deletedHeadValue = self.head.get_value() if self.head else None
    # print('self.head.get_next', self.head.get_next())
    self.head = self.head.get_next() if self.head else None
    if self.head == None:
      self.tail = None
    return deletedHeadValue


  def contains(self, value):
    """
    # for {for node in nodelist}
    #   search for me
    """
    node = self.head
    while node:
      if node.get_value() == value:
        return True
      else:
        node = node.get_next()        
    
    return False


  def get_max(self):
    node = self.head
    linked_listMax = -math.inf
    while node:
      if node.get_value() > linked_listMax:
        linked_listMax = node.get_value()
      else:
        node = node.get_next()        
    
    return linked_listMax if linked_listMax != -math.inf else None
