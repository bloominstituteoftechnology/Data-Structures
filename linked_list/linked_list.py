"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    #Node initiaizes with a single value and it's pointed set to none,
    #becuase it isn't pointing at anything.
    self.value = value
    self.next_node = next_node

  #returns the stored value
  def get_value(self):
    return self.value

  #returns the next node
  def get_next(self):
    return self.next_node

  #reset the pointer to a new node
  def set_next(self, new_next):
    self.next_node = new_next



class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
    if self.tail != None:
      self.tail = new_node
      self.tail.set_next(new_node)
    self.tail = new_node

####
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)
    if self.head == None: 
      self.head = new_node
    else:
      self.tail.set_next(new_node)
    self.tail = new_node
####


  def remove_head(self):
    if self.head == None: return None
    removed_value = self.head.get_value()
    self.head = self.head.get_next()
    return removed_value  


  def contains(self, value):
    
    current_node = self.head

    if current_node == None: return False
    if current_node.get_value() == value: return True

    while current_node.get_next() != None: 
      current_node = current_node.get_next()
      if current_node.get_value() == value: return True


  def get_max(self):
    # run a loop through the list
    current_node = self.head
    prev_node = None
    # break loop when next value is None
    while current_node.get_value() != None:
      #inside the loop, keep track of max value
      max_node = None
      prev_node = current_node.get_value()
      next_node = current_node.get_next()
      if(next_node > prev_node): 
        max_node = next_node
      else: 
        max_node = prev_node
    return max_node

    
    #return max value


    pass
