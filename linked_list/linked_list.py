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
  def __init__(self, head=None):
    self.head = head
    self.tail = None
    self.size = 0

  def get_size(self):
    return self.size

  def add_to_tail(self, value):
    new_node = Node(value, self.head)
    self.head = new_node
    self.size += 1
    pass

  def remove_head(self, value):
    this_node = self.head
    prev_node = None

    while this_node is not None:
      if this_node.get_value() == value:
        if prev_node is not None: # if we are not in the root node
          prev_node.set_next(this_node.get_next())
        else:
          self.head = this_node.get_next()
        self.size -= 1
        return True # data removed
      else:
        prev_node = this_node
        this_node = this_node.get_next()
    return False # data not found
    pass

  def contains(self, value):
    this_node = self.head # setting current node to root
    while this_node is not None:
      if this_node.get_value() == value:
        return value
      elif this_node.get_value() == None:
        return False
      else:
        this_node = this_node.get_next()
    pass

  def get_max(self):
    pass
