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
    node = Node(value)
    if self.tail is not None:
      self.tail.set_next(node)
    else:
      self.head = node
    self.tail = node

  def remove_head(self):
    if self.head is not None:
      new_head = self.head.get_next()
      del(self.head)
      self.head = new_head

  def contains(self, value):
    current_node = self.head
    while True:
      if current_node.get_next() == None:
        return False
      if current_node.get_value() == value:
        return True
      else:
        current_node = current_node.get_next()

  def get_max(self):
    if self.head is not None:
      current_node = self.head
      maximum = current_node
      while True:
        if current_node.get_value() > maximum.get_value():
          maximum = current_node
        if current_node.get_next() == None:
          return maximum.value
        else:
          current_node = current_node.get_next()
    else:
      return None


newList = LinkedList()

newList.add_to_tail('turtle')
newList.add_to_tail('porcupine')
newList.add_to_tail('walrus')
newList.add_to_tail('kookaburra')

print(newList.head.get_value())
print(newList.contains('walrus'))
print(newList.get_max())