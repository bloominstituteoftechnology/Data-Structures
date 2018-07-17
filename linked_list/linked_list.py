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

    if not self.head:
      self.head = node

    elif not self.head.next_node:
      self.head.set_next(node)

    else:
      self.tail.set_next(node)

    self.tail = node

  def remove_head(self):
    if self.head:
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    else:
        return None

  def contains(self, value):
    if self.head:
      i = self.head

<<<<<<< HEAD
      while i:
        if i.value == value:
          return True

        else:
          i = i.next_node

    else:
      return False
=======
  def contains(self, value):
    pass
>>>>>>> upstream/master

  def get_max(self):
    if self.head:
      i = self.head
      max_num = i.value

      while i:
        if i.value > max_num:
          max_num = i.value
          
        else:
          i = i.next_node

      return max_num

    else:
      return None
