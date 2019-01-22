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
    # 1. Create a new node
    # 2. Check if there is a current tail
    # 2-1. If there isn't a tail, then check if there is currently a head - if there isn't, we need the new node to be the tail and the head
    # 3. Else If there is a current tail (aka not None), set its next pointer to the new node
    # 3-1. Set the linked lists tail to the new node
    node = Node(value, None)
    if self.tail is None and self.head is None:
      self.tail = node
      self.head = node
    elif self.tail is not None:
      self.tail.next_node = node
      self.tail = node

  def remove_head(self):
    # 1. Check if there is a head
    # 1-1. If there is a head, check if there is a next node
    # 1-2. If there is a next node, set the next node to the new head
    # 2. Else if there isn't a next node, the current node is both the tail and head, derefence both
    if self.head is not None:
      head_to_remove = self.head.value
      if self.head.next_node is not None:
        self.head = self.head.next_node
      elif self.head.next_node is None:
        self.head = None
        self.tail = None
      return head_to_remove
    else:
      return None
    
  def contains(self, value):
    curr_node = self.head

    while True:
      if curr_node == None:
        return False
      elif curr_node.value == value:
        return True
      else:
        curr_node = curr_node.next_node

  def get_max(self):
    current_max = 0
    current_node = self.head
    
    while current_node is not None:
      if current_node.value > current_max:
        current_max = current_node.value
      current_node = current_node.next_node
    return current_max if current_max > 0 else None