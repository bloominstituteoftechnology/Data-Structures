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
    nn = Node(value)
    if not self.head:
      self.head = nn
      self.tail = nn
    else:
      self.tail.next_node = nn
      self.tail = nn

  def remove_head(self):
    #print("shv", self.head.value)
    if not self.head:
      return None

    if not self.head.next_node:
      head = self.head
      self.head = None
      self.tail = None
      return head.value
    else: 
      value = self.head.value
      self.head = self.head.next_node
      return value
    

  def contains(self, value):
    #check if list empty
    if not self.head:
      return None
    # assign the current node to variable
    current = self.head
    # iter through list
    while current:
      if current.value == value:
        return True
      #move on to next list node
      #by updating current
      current = current.get_next()
      # if we have gotten here then
      #the node we are looking for doesnt exist
    return False
#O(1n)
  def get_max(self):
    if not self.head:
      return None
    max_value = self.head.value
    #set current to heads' next
    current = self.head.get_next()
    while current: 
      if current.value > max_value:
        #update max_value
        max_value = current.value
      current = current.next_node
    return max_value
