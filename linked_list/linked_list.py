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
    newNode = Node(value)
    if self.head == None:
      self.head = newNode
      self.tail = newNode
      return
    else:
      self.tail.set_next(newNode)
      self.tail = newNode
    

  def remove_head(self):
    if self.head == None:
      return
    else:
      removed = self.head
      self.head = self.head.next_node
      return removed.value

  def contains(self, value):
    if self.head == None:
      return False
    else:
      def find_value(node):
        if node.value == value:
          return True
        elif node.next_node == None:
          return False
        else:
          return find_value(node.next_node)
      return find_value(self.head)


  def get_max(self):
    if self.head == None:
      return
    else:
      temp = 0
      def find_max(node, temp):
        if node == None:
          return temp
        elif node.value > temp:
          temp = node.value
          return find_max(node.next_node, temp)
        else:
          return find_max(node.next_node, temp)
      return find_max(self.head, temp)