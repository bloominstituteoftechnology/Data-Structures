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
    if self.head is None:
      self.head = Node(value)
    elif self.tail and self.head:
      self.tail.set_next(Node(value))
    self.tail = Node(value)

  def remove_head(self):
    if self.head:
      prev = self.head.value
      self.head = self.head.next_node
      return prev
    return None


  def contains(self, value):
    result = False
    if self.head:
        def node_contains(node):
          nonlocal result
          if node.value == value:
            result = True
          elif result == True:
            return result
          elif node.next_node:
            result = node_contains(node.next_node)
        node_contains(self.head)
        return result
    return result

  def get_max(self):
    maxx = None

    def maxx_func(node):
      if node.next_node is not None and node.next_node.value > maxx.value:
        maxx = node.next_node
      elif node.next_node is not None:
        maxx_func(node.next_node)
      else:
        return None
    if self.head:
      maxx = self.head
      maxx_func(maxx)
    return maxx.value or maxx
