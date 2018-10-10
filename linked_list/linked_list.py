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
    """Create a new node 
       Assign it's next reference to None
       Set the next reference of the tail to point to this new node.
       then update the tail reference itself to this new node. 
    """
    new_node = Node(value)
    new_node.set_next(None)
    self.tail.set_next(new_node)
    self.tail = new_node

  def remove_head(self):
    """
    set the head to the next node
    """
    
    next_in_line = self.head.get_next()
    self.head = next_in_line 

  def contains(self, value):
    pass

  def get_max(self):
    pass
