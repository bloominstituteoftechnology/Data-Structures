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
    if self.head = None:
        self.head = value
        self.tail = value
    else:
        self.tail.set_next = value
        self.tail = value

  def remove_head(self):
    if self.head == None:
        return
    else:
        next_head = self.head.next_node
        head_to_return = self.head
        self.head = next_head
        return head_to_return

  def contains(self, value):
    presently_searching_node = self.head
    while presently_searching_node != self.tail:
        if presently_searching_node == value:
            return true
        else:
            presently_searching_node = presently_searching_node.get_next
    if presently_searching_node == value:
        return true
    else:
        return false

  def get_max(self):
    current_max = -9999999999
    presently_searching_node = self.head
    while presently_searching_node != self.tail:
        if presently_searching_node.get_value > current_max:
            current_max = presently_searching_node.get_value
        else:
            presently_searching_node = presently_searching_node.get_next
    if presently_searching_node > current_max:
        current_max = presently_searching_node.get_value
    return current_max
