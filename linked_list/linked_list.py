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
    #Create new node
    #if the LinkList is not empty
    #Then set the tail's next to the new node
    #if it is empty, set the new node to the head
    #set the ll tail to the new node
    pass

  def remove_head(self):
    #Check if the head is None
    #set the head nodes next node value to a temp var
    #delete the head node
    #then set head to that temp
    pass

  def contains(self, value):
    pass

  def get_max(self):
    pass
