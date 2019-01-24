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

  # add an itme to the end of the list
  def add_to_tail(self, value):
    # if value is a proper node then turn it into one
    if not isinstance(value, Node):
      value = Node(value)

    # if it is an empty list, then add value as head of the list
    if self.head is None:
      self.head = value

    else:
      # if it is not a empty list, then add value as the tail of the list
      # self.tail.next = value
      self.tail.set_next(value)
    self.tail = value

    return

  def remove_head(self):
    if self.head:
      # if the next node from the head is empty
      if self.head.get_next() == None:
        # set temp_head to current head
        temp_head = self.head
        # set both the current head and current tail to be empty
        self.head = None
        self.tail = None
        # then return the temporary head
        return temp_head.get_value()
      else:
        # else set the temporary head to the current head
        temp_head = self.head
        # set the current head to the next node
        self.head = self.head.get_next()
        # return the temporary head
        return temp_head.get_value()
    else:
      # else return None
      return None

  def contains(self, value):
    # set self.head to current_head
    current_head = self.head
    # while the current_head
    while current_head:
      # if current_head has a value
      if current_head.get_value() == value:
        # return true
        return True
      # set current_head to the next node  
      current_head = current_head.get_next()
    # return false  
    return False

  def get_max(self):
    current_head = self.head
    # set maximum value to None
    max_value = None

    while current_head:

      # if max_value is None or current_head value is greater than max value
      if max_value is None or current_head.get_value() > max_value:

        # set max_value to value of current_head
        max_value = current_head.get_value()

      # set the current head to the next node of the current head
      current_head = current_head.get_value()

    # return max_value
    return max_value  