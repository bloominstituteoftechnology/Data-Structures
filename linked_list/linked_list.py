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
    if not self.head:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.set_next(new_node)
        self.tail = new_node

  def remove_head(self):
    if self.head:
        removed_head = self.head
        self.head = self.head.get_next()
        self.tail = None
        return removed_head.value

  def contains(self, value):
    node_being_searched = self.head #We start by checking the head value
    while node_being_searched:
        if node_being_searched.value == value:
            return True
        node_being_searched = node_being_searched.get_next() #node to be searched updated to next node
    return False

  def get_max(self):
    current_node = self.head
    if not current_node:
        return None

    max_value = current_node.value

    while current_node:
        if current_node.value > max_value:
            max_value = current_node.value

        current_node = current_node.get_next()

    return max_value
