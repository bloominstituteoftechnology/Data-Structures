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
    if self.tail is not None:
      self.tail.set_next(newNode)
    if self.head is None:
      self.head=newNode
    self.tail = newNode
    return

  def remove_head(self):
    if self.head is None:
      return self.head
    headCopy = self.head
    if self.head.get_next() is None:
      self.tail = None
    self.head=self.head.get_next()
    return headCopy.value
    

  def contains(self, value):
    if self.head is None:
      return False
    notFound = True
    currentNode = self.head
    while(notFound):
      if currentNode.value == value:
        notFound = False
      if currentNode == self.tail:
        if currentNode.value == value:
          return True
        return False
      currentNode = currentNode.next_node
    return True

  def get_max(self):
    if self.head is None:
      return None
    highestValue = self.head.value
    currentNode = self.head
    while(True):
      if currentNode.value > highestValue:
        highestValue = currentNode.value
      if currentNode == self.tail:
        break
      currentNode = currentNode.next_node
    return highestValue
    

    

