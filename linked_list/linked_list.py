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
      self.tail.set_next(node)
      self.tail = node

  def remove_head(self):
    if self.head is None:
      return None
    if not self.head.get_next():
      old_head = self.head
      self.head = None
      self.tail = None
      return old_head.get_value()
    else:
      head_value = self.head.get_value()
      self.head = self.head.get_next()
      return head_value

  def contains(self, value):
    current_node = self.head
    while True:
      if current_node is None:
        return False
      elif current_node.value == value:
        return True
      else:
        current_node = current_node.get_next()

  def get_max(self):
    # if not self.head:
    #   return None
    # max_node = self.head
    # current_node = self.head.get_next()
    # while current_node:
    #   if current_node.get_value() > max_node.get_value():
    #     max_node = current_node
    #   else:
    #     current_node = current_node.get_next()

    # return max_node.get_value()


    if self.head is not None:
      current_node = self.head.get_next()
      max_node = self.head
      while current_node:
        if self.head.get_next is None:
          return max_node.get_value()
        else:  
          if max_node.get_value() < current_node.get_value():
              max_node = current_node
          else:
              current_node = current_node.get_next()
      else:
          return max_node.get_value()
    else:
      return None


