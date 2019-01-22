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
    #create a new node
    node = Node(value) 
    # if the LL is not empty
    if self.tail is not None:
      #then set the tail's next to the new node
      self.tail.set_next(node)
    else:
      #if it is empty set the new node to the head
      self.head = node
      #set the LL's tail to the new node
    self.tail = node


  def remove_head(self):

    if self.head == None and self.tail == None:
      return None

    if self.head.next_node != None:
      return_val = self.head.value
      self.head = self.head.next_node
      self.tail = self.head.value
      # print(self)
      return return_val
    else:
      return_val = self.head.value
      self.head = None
      self.tail = None
      # print(self)
      return return_val

  def contains(self, value):
    #set the current node to the head
    curr_node = self.head
    #if the node is null return false
    while True:
      if curr_node is None:
        return False
      elif curr_node.value == value:
        return True
      else:
        curr_node = curr_node.next_node
    #else if the nodes value matches the query value return true
    #else set the current node to the tail and start from step 2

  def get_max(self):
    #loop through list starting at 0
    #declare variable for max number
    #if self is greater than self.next_node variable equals self
    if self.head == None:
      pass
    else:
      if self.head.value > self.tail.value:
        return self.head.value
      else:
        return self.tail.value
    
