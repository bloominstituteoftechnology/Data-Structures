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
    if (self.head == None):
      self.head = Node(value)
    else:
      current = self.head
      while (current.next != None):
          current = current.next
      current.next = Node(value)
    return self.head
  
  def remove_head(self):

      current = self.head
      while current:
          prev = current.next 
           
          del current.data
          current = prev 
 
  def contains(self, value):
    if self.head == None:
        return False
    else:
        x = self.head
        while x is not None:
            if p.data == data:
                return True
            x = x.next
        return False
=======
    pass

  def contains(self, value):
    pass


  def get_max(self):
    max_ = self.head[0]
    for item in self.head:
        if item > max_:
            max_ = value
    return max_  

