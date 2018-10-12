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
    # wrap it in a Node Instance
    new_node = Node(value, None)
    # Check if their is no head
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      # set the current tail's next reference to the new node
      self.tail.next_node(new_node)
      # update the List's tail reference
      self.tail = new_node

  def remove_head(self):
    # check to see if there is a head
    if not self.head:
      return None
    # check if the head node has a next node
    if not self.head.get_next():
      value = self.head.get_value()
      self.head = None
      self.tail = None
      return value
    else:
      value = self.head.get_value()
      self.head = self.head.get_next()
      return value

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the current node
    current = self.head
    # walk along the list so long as current is a Node
    while current:
      # return true if the current value we're looking at matches our target
      if current.get_value() == value:
        return True
      # update our current reference
      current = current.get_next()
    return False

  def get_max(self):
    max_value = 0
    cur_node = self.head
    if cur_node == None:
      self.tail = None
      return None
    else:
      while cur_node is not None:
        if cur_node.get_value() > max_value:
          max_value = cur_node.get_value()
        elif cur_node.get_value() < max_value:
          cur_node = cur_node.get_next()
    return max_value

  # def get_max(self):
  #   if not self.head:
  #     return None
  #   max_value = self.head.get_value()
  #   current = self.head .get_next()
  #   while current:
  #     if current.get_value() >  max_value:
  #       max_value = current.get_value()
  #     current