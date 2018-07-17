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
      self.tail.next_node = new_node
      self.tail = new_node
  
  # STRETCH
  # Adding a function for finding length

  def length(self):
    cur = self.head
    total = 0
    while cur.next!=None:
      total +=1
      cur = cur.next
    return total
  # Adding a display function for help
  def display(self):
    elems = []
    cur_node = self.head
    while cur_node.next!=None:
      cur_node = cur_node.next
      elems.append(cur_node.value)
    print (elems)

  def remove_head(self):
    if not self.head:
      return None
    if not self.head.next_node:
      head = self.head
      self.head = None
      self.tail = None
      return head.value
    else:
      value = self.head.value
      self.head = self.head.next_node
      return value

  def contains(self, value):
    if not self.head:
      return None
    current = self.head
    while current: 
      if current.value == value:
        return True
      current = current.get_next()
    return False

  def get_max(self):
    if not self.head:
      return None
    max_value = self.head.value
    current = self.head.get_next()
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.next_node
    return max_value
