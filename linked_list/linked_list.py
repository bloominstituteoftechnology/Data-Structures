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
    current = self.head
    found = False
    while found is False:
      if Node.get_next(current) == None:
        found = True
        Node.set_next(self.tail)
      else:
        current = Node.get_next(current)
      return self.tail 
    pass

  def remove_head(self):
    pass

  def contains(self, value):
    current = self.head
    found = False
    while current and found is False:
      if Node.get_value(current) == value:
        found = True
      else: 
        current = Node.get_next(current)
    if current== None:
      raise ValueError("Value not in list")
    return current

  def get_max(self):
    pass


node1 = Node(13)
# print(node1.value)

list1 = LinkedList()
# print(list1.head)
# print(list1.tail)
