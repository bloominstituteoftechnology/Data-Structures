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
    create_node = Node(value)

    if self.head:
      self.tail.set_next(create_node)
    else:
      self.head = create_node
    
    self.tail = create_node


    

  def remove_head(self):
    # --> If no head, return None
    # --> Check if there is a next node
    #   --> If there is: create variable to store the head's value || set the head to the next head and return the value
    #   --> Else: store old head value, set new head to None, and set tail to None
    if not self.head:
      return None

    if self.head.get_next():
      value = self.head.get_value()
      self.head = self.head.get_next()
      return value
    else:
      head = self.head
      self.head = None
      self.tail = None
      return head.get_value()

  def contains(self, value):
    current_node = self.head

    if not current_node:
      return False    

    while current_node:
      if current_node.get_value() == value:
        return True

      current_node = current_node.get_next()

  def get_max(self):    
    if not self.head:
      return None

    max_value = self.head.get_value()
    current = self.head.get_next()

    while current:
      if current.get_value() > max_value:
        max_value = current.get_value()

      current = current.get_next()
      
    return max_value
         

      

        
