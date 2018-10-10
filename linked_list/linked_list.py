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
    new_node=Node(value)
    if self.head==None:
      self.head=new_node
      self.tail=new_node
    elif self.head.get_next()==None:
      self.tail=new_node
      self.head.set_next(self.tail)
    else:
      self.tail.set_next(new_node)
      self.tail=new_node

  def remove_head(self):
    decapitated_head=self.head
    if self.head==None:
      return None
    elif self.head.get_next()==None:
      self.head=None
      self.tail=None
    else:
      self.head=self.head.get_next()
    return decapitated_head.get_value()

  def contains(self, value):
    if self.head==None:
      return False
    element=self.head
    while True:
      if element.get_value()!=value and element.get_next()==None:
        return False
      elif element.get_value()==value:
        return True
      else:
        element=element.get_next()

  def get_max(self):
    if self.head==None:
      return None
    element=self.head
    max=element.get_value()
    while True:
      if element.get_value()>max:
        max=element.get_value()
      if element.get_next()==None:
        return max
      else:
        element=element.get_next()