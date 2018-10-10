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
    node = Node(value)
    if self.head is None:
      self.head = node
      self.tail = node

    elif self.tail and self.head:
      old_tail = self.tail
      old_tail.set_next(Node(value))
    self.tail = node

  def remove_head(self):
    if self.head is None:
      return None
    elif self.head.next_node is None:
      current = self.head
      self.head = None
      self.tail = None
      return current.value
    else:
      current = self.head
      self.head = current.next_node
      current.next_node = None
      return current.value


  def contains(self, value):
    result = False
    if self.head is not None:
      def node_contains(node):
        val = node.value
        if val == value:
          result = True
          return result
        if result == True:
          return True
        elif node.next_node is None:
          return False
        else:
          result = node_contains(node.next_node)
        node_contains(self.head)
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
