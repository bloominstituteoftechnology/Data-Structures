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
    if self.tail is not None:
      self.tail.next_node = Node(value)
      self.tail = self.tail.next_node
    else:
      self.tail = Node(value)
      self.head = self.tail

  def remove_head(self):
    if self.head == None:
      return None
    else:
      removed_head = self.head.value
      self.head = self.head.next_node
      return removed_head

  def contains(self, value):
    current = self.head
    while current is not None:
      if current.value == value:
        return True
      else:
        current = current.next_node
    return False

  def get_max(self):
    if self.head == None:
      return None
    current = self.head
    max_value = self.head.value
    while current is not None:
      if current.value > max_value:
        max_value = current.value
      current = current.next_node
    return max_value


list = LinkedList()

list.add_to_tail(10)
list.add_to_tail(20)
print(list.head)
print(list.tail)
print(list.head.next_node)
list.remove_head()
print(list.head)
print(list.contains(10))
list.remove_head()
print(list.head)
print(list.contains(20))
list.remove_head()
print(list.head)