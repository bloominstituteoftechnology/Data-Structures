import sys
sys.path.append('../queue')
from queue import Queue

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

  def get_values(self):
    current_node = self.head
    values = []
    while current_node:
      values.append(current_node.value)
      current_node = current_node.next_node
    return values

  def add_to_tail(self, value):
    new_node = Node(value)
    if not self.head and not self.tail:
        self.head = new_node
        self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node
      
  def remove_head(self):
    node_to_delete = self.head
    if not self.head:
        return None
    elif self.tail == self.head:
        self.tail = None
        self.head = None
        return node_to_delete.value
    else:
      self.head = self.head.next_node
      node_to_delete.next_node = None
      return node_to_delete.value

  def remove_tail(self):
    node_to_delete = self.tail
    current_node = self.head
    if not self.tail:
      return None
    elif self.tail == self.head:
      self.tail = None
      self.head = None
      return node_to_delete.value
    else:
      while current_node.next_node:
        if current_node.next_node == self.tail:
          current_node.next_node = None
          self.tail = current_node
          return node_to_delete.value
        current_node = current_node.next_node

  def contains(self, value):
    current_node = self.head
    found = False
    while current_node:
        if current_node.value == value:
          found = True
        current_node = current_node.next_node
    return found

  def get_max(self):
      if not self.head:
        return None
      else:
        current_node = self.head
        max = current_node.value
        while current_node:
          if current_node.value > max:
            max = current_node.value
          current_node = current_node.next_node
        return max

  def make_reversed_version(self):
    reversed_node_values = []
    if self.head:
      current_node = self.head
      while current_node:
        reversed_node_values.insert(0, current_node.value)
        current_node = current_node.next_node
      reversed_list = LinkedList()
      for i in range(len(reversed_node_values)):
        reversed_list.add_to_tail(reversed_node_values[i])
      return reversed_list
    else:
      return "Cannot reverse an empty list!"


linked_list = LinkedList()
linked_list.add_to_tail(10)
linked_list.add_to_tail(20)

values = linked_list.get_values()
print(values)
reversed_linked_list = linked_list.make_reversed_version()
print(reversed_linked_list)
print(reversed_linked_list.head.value, reversed_linked_list.tail.value)
print(reversed_linked_list.get_values())
# linked_list.remove_tail()
# new_values = linked_list.get_values()
# print(new_values)
# contains_twenty = linked_list.contains(20)
# print(contains_twenty)
# max = linked_list.get_max()
# print(max)