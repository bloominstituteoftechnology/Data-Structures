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
    new_node = Node(value)

    if self.tail == None:
      try:
        self.head = new_node
      except:
        self.head.next_node = new_node
    else:
      self.tail.next_node = new_node

    self.tail = new_node

  # # From Sean
  # new_node = Node(value)
  # if not self.head:
  #   self.head = new_node
  #   self.tail = new_node  # Never forgat the tail
  # else:
  #   # We have a non-empty list
  #   # Setthing the last node's 'next' to the new node
  #   self.tail.next_node = new_node
  #   # Update the linked list's 'tail' reference
  #   self.tail = new_node

  def remove_head(self):
    # if self.head != None:
    #   try:
    #     self.head = self.head.next_node
    #   except:
    #     self.head = None
    # else:
    #   return None

  # From Sean
  # First check if there is no head
    if not self.head:
      return None
    # if head has no 'next', ther we have a single element
    if not self.head.next_node:
      # take a reference to the current head
      head = self.head
      # delete the list's head reference
      self.head = None
      # also make sure the tail points to None
      self.tail = None
      return head.value
    else:
      # we have multiple elements in our list
      value = self.head.value
      self.head = self.head.next_node
      return value

  def contains(self, value):
    # contain = False
    # pointer = self.head

    # while pointer != None:
    #   if pointer == value:
    #     contain = True
    #   pointer = pointer.next_node

    # return contain

    # From Sean
    # check to see if our list is empty
    if not self.head:
      return None
    # assign the current node to a variable
    current = self.head
    #iterate through the list
    while current:
      if current.value == value:
        return True
      # move on to the next list node
      # by updating 'current'
      current = current.get_next()
    # if we've gotten here, then the node we're looking for is not in our list
    return False

    

  def get_max(self):
    # From Sean
    if not self.head:
      return None
    max_value = self.head.value
    # set current to head's 'next'
    current = self.head.get_next()
    while current:
      if current.value > max_value:
        # update max_value
        max_value = current.value
      current = current.next_node
    return max_value
