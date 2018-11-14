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
    # create the next node with the value
    next_node = Node(value)

    # if we are not the head
    if not self.head:
      # set the head to next node
      self.head = next_node
      # and set the tail to next node
      self.tail = next_node
    else:
      # otherwise set the address of next node on the tail 
      self.tail.set_next(next_node)
      # and set the tail to the next node
      self.tail = next_node

  def remove_head(self):
    # if we are the head
    if self.head:
      # if the next node of the head is empty
      if self.head.get_next() == None:
        # set up a temporary head to current head
        temp_head = self.head
        # empty off the current head and the current tail
        self.head = None
        self.tail = None
        # then return the temporary head (like popping it off)
        return temp_head.get_value()
      else:
        # otherwise set the temporary head to the current head
        temp_head = self.head
        # and set the current head to the next node
        self.head = self.head.get_next()
        # then return the temporary head (like popping it off)
        return temp_head.get_value()
    else:
      # otherwise just return nothing / None
      return None

  def contains(self, value):
    pass

  def get_max(self):
    pass
