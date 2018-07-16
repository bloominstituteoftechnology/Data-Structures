from pprint import pprint

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
    newNode = Node(value)
    if self.head == None:
      self.head = newNode
    else: self.tail.next_node = newNode
    self.tail = newNode

  def remove_head(self):
    if self.head == None:
      return None
    else:
      old_head = self.head 
      self.head = self.head.next_node
      return old_head.value

    # if self.head != None:
    #   old_head = self.head 
    #   self.head = self.head.next_node
    #   return old_head.value
    # return None

  def contains(self, value):
    currentNode = self.head
    while currentNode:
      if currentNode.value == value:
        return True
      currentNode = currentNode.next_node
    return False

  def get_max(self):
    if self.head == None:
      return None
    currentNode = self.head
    biggest = self.head.value
    while currentNode != None:
      if currentNode.value > biggest:
        biggest = currentNode.value
      currentNode = currentNode.next_node
    return biggest
