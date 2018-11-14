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
    if not self.head:
      self.head = node
      self.tail = node
      return
    else:
      if self.head == self.tail:
        self.head.set_next(node)
      else:
        self.tail.set_next(node)
    self.tail = node

  def remove_head(self):
    if self.head:
      old_head = self.head
      new_head = self.head.get_next()
      self.head = new_head
      if old_head == self.tail:
        self.tail = new_head
      return old_head.value
    else:
      return None

  def contains(self, value):
    node_checked = self.head
    while node_checked != None:
      if node_checked.get_value() == value:
        return True
      else:
        node_checked = node_checked.get_next()
    return False


  def get_max(self):
    max = 0
    node_checked = self.head
    while node_checked:
      if node_checked.value > max:
        max = node_checked.value
      node_checked = node_checked.get_next()
    return max if max else None