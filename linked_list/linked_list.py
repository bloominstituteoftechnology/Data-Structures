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
    # Assigning new_node
    new_node = Node(value)
    # Checking the existance of the head
    if not self.head:
      self.head = new_node
    # Tail
      self.tail = new_node

    else:
    # Setting last node 'next' to new node
      self.tail.next_node = new_node
    # and now need to update the tail reference
      self.tail = new_node

  def remove_head(self):
    # checking the head
    if not self.head:
      return None
    # Checking if the head is only a single element
    if not self.head.next_node:
      # The getting ref of the current head
      head = self.head
      # deleting head reference
      self.head = None
      # tail points to none
      self.tail = None
      return head.value
    else:
      # now checking if there are multiple nodes in the list
      value = self.head.value
      self.head = self.head.next_node
      return value

  def contains(self, value):
    # checking if there are values in the list
    if not self.head:
      return None
    # assign current node to var
    current_node = self.head
    # go through the list
    while current_node:
      if current_node.value == value:
        return True
    # move to the next  node in the list
    # also updating current
      current_node = current_node.get_next()
    return False

  def get_max(self):
    if not self.head:
      return None
    maximum_value = self.head.value
    # setting current head to next
    current_head = self.head.get_next()
    while current_head:
      if current_head.value > maximum_value:
        # Updating maximum value
        maximum_value = current_head.value
      current_head = current_head.next_node
    return maximum_value
