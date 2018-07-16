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
    new_node = Node(1)
    if self.head == None: 
      self.head = Node(value)
      self.tail = self.head
      print(f'The head is equal to {self.tail.value}.')
    elif self.head.next_node == None:
      new_node = Node(value)
      self.head.set_next(new_node)
      self.tail = new_node
      print(f'The next value after the head is equal to {self.tail.value}.')
    elif new_node.next_node == None: 
      new_node.set_next(Node(value))
      new_node = Node(new_node.get_next().value)
      self.tail = new_node
      print(f'The next value is {self.tail.value}.')
  
  def remove_head(self):
    pass

  def contains(self):
    pass

  def get_max(self):
    pass

a = LinkedList()
a.add_to_tail(1)
a.add_to_tail(2)
a.add_to_tail(3)
a.add_to_tail(4)
a.add_to_tail(5)
a.add_to_tail(6)
a.add_to_tail(7)
a.add_to_tail(8)
a.add_to_tail(9)
a.add_to_tail(10)
a.add_to_tail(11)
a.add_to_tail(12)