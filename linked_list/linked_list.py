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
        return
    else:
        self.tail.next_node = new_node
        self.tail = new_node
        return

  def remove_head(self):
    if self.head == None:
      return None
    elif self.head == self.tail:
      self.head = None
      self.tail = None
      return self.head.value
    else:
      new_head = self.head.next_node
      self.head = new_head
      return

  def contains(self, value):
    if self.head == None:
      return False
    else:
      current_node = self.head
      while current_node is not None:
        if current_node.value == value:
          return True
        else:
          current_node = current_node.next_node
      return False


  def get_max(self):
    if self.head == None:
      return None
    else:
      current_node = self.head
      max_value = 0
      while current_node is not None:
        if current_node.value > max_value:  
          max_value = current_node.value
          current_node = current_node.next_node
      return max_value

l1 = LinkedList()
l1.add_to_tail(5)
l1.add_to_tail(7)
l1.add_to_tail(8)
l1.remove_head()
print(l1.contains(8))
print(l1.head.value)
print(l1.get_max)