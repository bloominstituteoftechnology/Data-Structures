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

class LinkedList(): #properties are head and tail
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value): #replaces the tail with a new value that is passed on    
      new_node = Node(value) #new instance of node class
      if not self.head: #if the list is empty:
        self.head = new_node #both self.head and self.tail will be assigned new node
        self.tail = new_node
      elif self.head == self.tail:  #if self.tail and self.head are the same:
        self.tail.next_node = new_node #self.tail.next_node is another node instance of new node
        self.tail = new_node
  def remove_head(self): #removes and returns the head node
      # self.head = self.next_node
      if not self.head:
        return None
      elif not self.head.next_node:
        head = self.head
        self.head = None
        self.tail = None
        return head.value
      else:
        value = self.head.value
        self.head = self.head.next_node
        return value
      

  def contains(self, value): #similar to includes in .js
      # check to see if list is empty
      if not self.head:
        return None
      pointer = self.head
      while pointer:
        if pointer.value == value:
          return True
        else:
          pointer = pointer.next_node
      
      return False

<<<<<<< HEAD
  def get_max(self): #get max value in entire list
      if not self.head:
        return None
      max_value = self.head.value
      pointer = self.head.get_next()
      while pointer:
        if pointer.value > max_value:
          max_value = pointer.value
        else:
          pointer = pointer.next_node
      return max_value
      
=======
  def contains(self, value):
    pass

  def get_max(self):
    pass
>>>>>>> f1923a145d435024809791b767a552924cfaada7
