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
    new_tail = Node(value)
    if not self.head:
      self.tail = new_tail
      self.head = new_tail
    else:
      self.tail.set_next(new_tail)
      self.tail = new_tail

  def remove_head(self):
      if self.head != None:
        value = self.head.get_value()
        if self.head.get_next() != None:
          self.head = self.head.get_next()
        else:
          self.head = None
          self.tail = None
        return value
  
  def contains(self, value):
    node_value = self.head
    while node_value: 
      if node_value.get_value() == value:
        return True
      elif node_value.get_next() == None:
        return False
      node_value = node_value.get_next()
  
  def get_max(self):
    if self.head == None:
      return None
    node_value = self.head
    max_value = node_value.get_value()
    
    while node_value != None:
      if node_value.get_value() > max_value:
        max_value = node_value.get_value()
      else:
        node_value = node_value.get_next()
    return max_value



list1= LinkedList()
list1.add_to_tail(10)
list1.add_to_tail(20)
list1.add_to_tail(24)
#print(list1.tail.get_value())
print(list1.get_max())