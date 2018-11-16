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

  def __repr__(self):
    output = ""
    marker = self.head
    while marker:
      output += (f"{marker.get_value()} -> ")
      marker = marker.get_next()
    output += "None"
    return output

  def add_to_tail(self, value):
    new = Node(value, None)
    # if there is a tail, then set its next_node to the new node
    if self.tail:
      self.tail.set_next(new)
    self.tail = new
    # if there is no head, then set the head to the new node
    if not self.head:
      self.head = new


  def remove_head(self):
    if not self.head:
      return None

    old_head = self.head
    self.head = old_head.get_next()
    old_head.set_next(None)
    if old_head == self.tail:
      self.tail = None

    if old_head:
      return old_head.value
    


  def contains(self, value):
    marker = self.head
    while marker:
      if marker.get_value() == value:
        return True
      marker = marker.get_next()
    return False

  def get_max(self):
    marker = self.head
    if not marker:
      return None
    max = marker.get_value()
    while marker:
      if marker.get_value() > max:
        max = marker.get_value()
      marker = marker.get_next()
    return max

