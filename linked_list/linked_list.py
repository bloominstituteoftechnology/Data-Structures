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
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.set_next(newNode)
      self.tail = newNode

  def remove_head(self):
    if self.head is not None:
      currHead = self.head
      prevHead = None
      found = False
      while currHead and found is False:
          if currHead.get_data() == data:
            found = True
          else:
            prevHead = currHead
            currHead = currHead.get_next()
    elif currHead is None:
      raise ValueError("No data is found")
    if prevHead is None:
      self.head = currHead.get_next()
    else:
      prevHead.set_next(currHead.get_next())


  def contains(self, value):
    currHead = self.head
    found = False
    while currHead and found is False:
      if currHead.get_value() == value
        found = True
      else:
        currHead = currHead.get_next()
    if currHead is None:
      raise ValueError("No data in list")
    return found

  def get_max(self):
    pass
