
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
    self.max = None

  def add_to_tail(self, value):
    node = Node(value)
    if self.tail is not None:
      self.tail.set_next(node)
      self.tail = node 
      if self.max.value < node.value:
        self.max = node
    else:
      self.head = node 
      self.tail = node
      self.max = node

  def remove_head(self):
    if self.head is not None:
      new_head = self.head
      del(self.head)
      self.head = new_head.next_node

      if self.head is None:
        self.tail = None
      return new_head.value


  def contains(self, value):
    curr_node = self.head
    while True:
      if curr_node is None:
        return False
      elif curr_node.value == value:
        return True
      else:
        curr_node = curr_node.next_node

  def get_max(self):
<<<<<<< HEAD
    if self.max is not None:
      return self.max.value
    else:
      return None
=======
    pass
 
>>>>>>> 9ca0284d785b74c08b440f6ddf3ed2d8afc977c2
