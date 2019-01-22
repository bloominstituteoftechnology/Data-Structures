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
    # create a new node
    node = Node(value)
    # If the LL is not empty
    if self.tail is not None:
      # Then set the tail's next to the new node
      self.tail.set_next(node)
    else:
      # If it's empty, set the new node to the head
      self.head = node
    # Set the LL's to the new node
    self.tail = node

  def remove_head(self):
    # Check if the head is None
    if self.head is not None:
      # set the head nodes next node value to a temp var
      new_head = self.head.next_node
      # delete the head node
      del(self.head)
      # then set head to the temp
      self.head = new_head

  def contains(self, value):
    # Set the current node to the head
    curr_node = self.head
    while True:
      # 1. If the node is null, return False
      if curr_node is None:
        return False
      # 2. Else, if the node's value matches the query value, return True
      elif curr_node.value == value:
        return True
      # 3. Otherwise, set the current node to the tail and start from step 1
      else:
        curr_node = curr_node.next_node

  def get_max(self):
    pass
