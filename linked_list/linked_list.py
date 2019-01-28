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
    node = Node(value)

    #if the LinkList is not empty
    #Then set the tail's next to the new node
    if self.tail is not None:
      self.tail.set_next(node)


    #if it is empty, set the new node to the head
    else:
      self.head = node

    #set the ll tail to the new node
    self.tail = node

  def remove_head(self):
    #Check if the head is None
    if self.head is not None:
    #set the head nodes next node value to a temp var
      new_head = self.head.next_node
    #delete the head node
    #then set head to that temp
      self.head = new_head
    
  def contains(self, value):
    # start at head
    curr_node = self.head

    while True:
      #if node is null, return false
      if curr_node is None:
        return False
      
      elif curr_node.value == value:
        return True

      else:
        curr_node = curr_node.next_node
    

  def get_max(self):
    #set start to head
    start = self.head
    #set current max to value of head
    cur_max = start.get_value()
    #while head is not empty
    while start:
      # if current max is less than next value
      # assign greater value to current max
      # go to next value
      if cur_max < start.get_value():
        cur_max = start.get_value()
      start = start.get_next()

    return cur_max
