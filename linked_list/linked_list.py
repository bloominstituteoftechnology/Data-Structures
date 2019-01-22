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
    new_node = Node(value)    # create a new node and put in value
    if self.head == None:     # if linked list is empty 
      self.head = new_node    # make new node for head
      self.tail = new_node    # make new node for tail
    else:
      self.tail.next_node = new_node    # create new node after tail
      self.tail = self.tail.next_node   # set new node as new tail

  def remove_head(self):
    removed = self.head                 # assign removed to head
    if self.head == None:               # if linked list is empty
      return None                       # return None
    elif self.head.next_node == None:   # if head next node is empty
      self.head = None                  # head is empty (when head value is removed)
      self.tail = None                  # tail is empty
    else:
      self.head = self.head.next_node   # set new head and head next node
    return removed.value                # removed head value

  def contains(self, value):
    if self.head == None:         # if linked list is empty  
      return False                # return False
    else:
      node = self.head            # assign node to head
      while node is not None:     # while node is not empty
        if node.value == value:   # if the node value is equal to value
          return True             # return True
        node = node.next_node     # assign node as the next node (move on to next node)
      return False                # return False

  def get_max(self):
    if self.head == None:             # if linked list is empty
      return None                     # return None
    else:
      start = self.head               # assign start to head
      largest = self.head.value       # assign largest to the head value
      while start:                    # while start is not None
        if start.value > largest:     # if start value is greater than largest (head value)
          largest = start.value       # assign largest as the start.value
        start = start.next_node       # assign start to the next node
      return largest                  # return largest