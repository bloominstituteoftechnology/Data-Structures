"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node: #represents a single node
  def __init__(self, value=None, next_node=None): #value and next_node default point to None
    self.value = value #linked list value that's stored inside node
    self.next_node = next_node #next node in linked list. if no other node in list then it will point to None.

  def get_value(self): #gets value of node
    return self.value

  def get_next(self): #gets value of next_node
    return self.next_node

  def set_next(self, new_next): #sets next_node to new_next
    self.next_node = new_next

class LinkedList(Node): #properties are head and tail
  def __init__(self):
    self.head = None
    self.tail = None
    super().__init__(value = None, next_node = None)

  def add_to_tail(self, value): #replaces the tail with a new value that is passed on    
      node = Node(value) #new instance of node class
      if self.head == None: #if the list is empty:
        self.head = node #both self.head and self.tail will be assigned node
        self.tail = node
      elif self.head == self.tail:  #if self.tail and self.head are the same:
        self.tail = node #self.tail is the node instance
        self.head.next_node = node #self.head.next_node is another node instance
    
  def remove_head(self): #removes and returns the head node
      # self.head = self.next_node
      if self.head == None:
        return None
      elif self.head == self.tail:
        done = self.head
        self.head = None
        self.tail = None
        return done.value
      else:
        done = self.head
        self.head = self.head.next_node
        return done.value
      

  def contains(self, value): #similar to includes in .js
      # linked_list = LinkedList(self)
      pass
  
  def get_max(self): #get max value in entire list
    max_value = self.head
    if self.head == self.tail:
      max_value = self.head
    elif self.head == None:
      max_value = None
    elif self.head > max_value:
      max_value = self.head
    else:
        return max_value

