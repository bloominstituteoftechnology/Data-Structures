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

    if self.tail is None or self.head is None:
      self.head = node
    else:
      self.tail.set_next(node)

    self.tail = node

  def remove_head(self):
    print(self.head)
    print(self.tail)
    if self.head is not None:
      prev_value = self.head.value
      self.head = self.head.get_next()

      if self.head is None:
        self.tail = None

      return prev_value
    else:
      return None

  def contains(self, value):
    curr_node = self.head

    while True:
      if curr_node is None:
        return False
      elif curr_node.get_value() == value:
        return True
      else:
        curr_node = curr_node.get_next()

  def get_max(self):
    if self.head is None:
      return None

    max_value = self.head
    curr_node = self.head

    while True:
      if curr_node is None:
        return max_value.get_value()
      elif curr_node.get_value() > max_value.get_value():
        max_value = curr_node

      curr_node = curr_node.get_next()