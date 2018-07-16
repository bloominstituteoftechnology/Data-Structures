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

  def add_to_tail(self, value): # add a new node to the end
    new_node = Node(value)
    if self.tail == None: # Checking to see if Tail is empty
      if self.head == None: # checking if Head is empty
        self.head = new_node # setting head to the newly created node
      else:
        self.head.next_node = new_node #the next (the tail) will become the new node
    else:
      self.tail.next_node = new_node #the new node becomes the tail if tail is empty
    self.tail = new_node #points to newly added tail
    

  def remove_head(self): # Gets rid of the head node and returns the new head node
    curr = self.head #grabbing the current head
    new_head = curr.next_node #grabbing the next node
     #checking to see if there is a head
    if curr: #When there is a head
      self.head = new_head #setting the second node to new head
      return curr.value 
    else: #if there is no head
      return False #reurn false

  def contains(self): #See if linked list contains a certain value
    pass

  def get_max(self): # returns the highest valued node 
    pass
