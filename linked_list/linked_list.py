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
    if self.head is None:
        self.head = node
        self.tail = node
    else:
        self.tail.next_node = node
        self.tail = node

  def remove_head(self):
    if self.head == None:
        return None
    else:
        node = self.head
        self.head = node.get_next()
        self.tail = None
        return node.value

  def contains(self, value):
    node = self.head
    if node is None:
        return False
    while node:
        if node.value == value:
            return True
        node = node.next_node
    return False
        

  def get_max(self):
    node = self.head
    if node is None:
        return
    max = 0
    while node:
        if node.value > max:
            max = node.value
        node = node.next_node
    return max
