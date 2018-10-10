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
    if self.head == 0:
      return None
    else:
      self.tail = Node(value)

  def remove_head(self):
    if self.head == 0: 
      return None
    else:
      self.head = self.head.get_next()

  def contains(self, value, node="start"):
    # L = LinkedList
    node = self.head if node == "start" else node

    if node != None:
      node_value = node.get_value()
      if node_value == value:
        return True
      else:
        next_node = node.get_next()

        return self.contains(value, next_node)
      # if get_naxt 
    else:
      return False

  # def get_max(self):
  #   # need reference point 
  #   max = self.head
  #   for key, value in LinkedList:
  #     if value > max:
  #       max = value
