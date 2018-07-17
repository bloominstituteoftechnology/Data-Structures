"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
from numpy import inf

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
    if(self.head == None): 
      self.tail = Node(value)
      self.head = self.tail
    elif(self.head == self.tail):
      self.head.set_next(Node(value))
      self.tail = self.head.get_next()
    else:
      cur_node = self.head.get_next()

      while(cur_node.getnext() != None):

        cur_node = cur_node.get_next()

      cur_node.set_next(Node(value))
      self.tail = cur_node.get_next()


  def remove_head(self):
    self.head = self.head.get_next()

  def contains(self, value):
    cur_node = self.head

    while(cur_node.get_next() != None):
      if(cur_node.get_value == value):
        return True
      else:
        cur_node = cur_node.get_next()

  def get_max(self):
    max = inf
    cur_node = self.head

    while(cur_node.get_next() != None):
      if(cur_node.get_value > max):
        max = cur_node.get_value()
        cur_node = cur_node.get_next()
      else:
        cur_node = cur_node.get_next()
