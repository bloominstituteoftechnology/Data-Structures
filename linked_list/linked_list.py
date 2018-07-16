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
    if self.head == None: 
      head = Node(value)
    elif self.head.next_node == None:
      head.set_next(value)
      current_node = Node(head.get_next())
    elif current_node.next_node == None: 
      current_node.set_next(value)
      current_node = Node(current_node.get_next())

      
         
          
          


  def remove_head(self):
    pass

  def contains(self):
    pass

  def get_max(self):
    pass

a = LinkedList()
b = a.add_to_tail(1)
print(b)
