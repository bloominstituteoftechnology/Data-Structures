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
    new_node = node(value)
    cur = self.head

    while cur.next != None:
      cur = cur.next
    cur.next = new_node
  
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
    pass

  def contains(self, value):
    pass

  def get_max(self):
    pass
