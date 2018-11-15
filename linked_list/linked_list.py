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
    if self.head is None:
      self.head=new_node
      self.tail=new_node
    else:
      self.tail.set_next(new_node)
      self.tail=new_node

  def remove_head(self):
    to_remove =self.head
    if to_remove is None:
      return None
    elif to_remove == self.tail:
      self.head = None
      self.tail = None
      return to_remove.value

    else:
      self.head = self.head.next_node
      return to_remove.value

      

  def contains(self, value):
      temp=self.head
      while temp:
        if temp.value == value:
          return True
        temp=temp.next_node
      return False
    

  def get_max(self):
    if self.head is None:
       return None
    else:
      list_max = self.head.value
      temp = self.head
      while temp:
          if temp.value > list_max:
              list_max = temp.value
          temp = temp.next_node
      return list_max
