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
      new_node = Node(value)
      if self.head == None:
        self.head = new_node
        self.tail = new_node
        self.head.set_next(self.tail)
      else:  
        self.tail = new_node
      pass

  def remove_head(self):
    print(self.head.value)
    nextt = self.head.get_next()
    print(nextt.value)
    print(self.head.value)
    print(self.tail.value)
    pass

  def contains(self, value):
    pass

  def get_max(self):
    pass

#notes for refrence
  # def add_to_tail(self, value):
  #     # print(self.tail, '-- self.tail A')
  #     # print(self.head, '-- self.head A')
  #     new_node = Node(value)
  #     # print(new_node.get_value(), '-- new_node value')
  #     if self.head == None:
  #       # print('no head', new_node)
  #       self.head = new_node
  #       # print(self.head, '-- self.head B')
  #       # print(self.head.value, '-- self.head C')
  #       self.tail = new_node
  #       # print(self.tail.value, '-- self.tail.value B')
  #       self.head.set_next(self.tail)
  #       # print(self.head.get_next(), '-- self.head D')
  #     else:  
  #       self.tail = new_node
  #       # print(self.tail.value, '-- self.tail B')
  #     pass