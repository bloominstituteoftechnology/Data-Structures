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
    #wrap it in a Node instance
    new_node = Node(value, None)
    #check if there is no head
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      #set the current tail's next refernce to the new node
      self.tail.set_next(new_node)
      #update the list's tail reference
      self.tail = new_node

  def remove_head(self):
    #check to see if there is a head
    if not self.head:
      return None
    #check if the head node has a next node
    if not self.head.get_next():
      value = self.head.get_value()
      self.head = None
      self.tail = None
      return value
    else:
      value = self.head.get_value()
      self.head = self.head.get_next()
      return value

  def contains(self, value):
    if not self.head:
      return False
    #get a reference to the current node
    current = self.head
    #walk along the list so long as current is a node
    while current:
      #return true if the current value we're looking at matches our target
      if current.get_value() == value:
        return True
      #update our current reference
      current = current.get_next()
    return False

  def get_max(self):
    #similar to what we did in contains
    #iterate along the list
    if not self.head:
      return None
    #reference to max value that we've seen
    #initialize max_value to self.head.get_value()
    max_value = self.head.get_value()
    #set current to get_next to set it to the heads next node
    current = self.head.get_next()
    #loop while current is a valid node
    while current:
      #check to see if current.get_value() is bigger than max value
      if current.get_value() > max_value:
        max_value = current.get_value()
      current = current.get_next()
    return max_value