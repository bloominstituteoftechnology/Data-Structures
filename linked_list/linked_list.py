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
  def contains(self, value):
    self.head = None
    self.tail = None

  def add_to_tail(self, value): # add a new node to the end
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      return 
    last = self.head
    while (last.next):
      last = last.next
      
    last.next = new_node
    

  def remove_head(self): # Gets rid of the head node and returns the new head node
    prev = None
    curr = self.head
    while curr:
      if curr.getData() == value:
        if prev: 
          prev.setNextNode(curr.getNextNode())
        else:
          self.head = curr.getNextNode()
        return curr
      
      prev = curr
      curr = curr.getNextNode()
    
    return False

  def contains(self): #See if linked list contains a certain value
    pass

  def get_max(self): # returns the highest valued node 
    pass
