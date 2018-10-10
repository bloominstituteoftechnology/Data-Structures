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
   
    # print(self.head.value, '-- self.head After')

    if self.head == None:
      print('no head')
      # self.tail.next_node = None
    else:  
      print('no tail')
      print(self.tail, '-- self.tail OG')
      print(self.head, '-- self.tail OG')
      new_node = Node(value)
      new_node.set_next(self.tail)
      print(new_node.get_value(), '-- new_node value')
      self.tail = new_node
      print(self.tail.value, '-- self.tail After')
    pass

  def remove_head(self):
    pass

  def contains(self, value):
    pass

  def get_max(self):
    pass
