
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

    elif self.head != None:
      self.tail.next_node = newNode
      self.tail = self.tail.next_node

  def remove_head(self):
    if self.head != None:
      return_value = self.head.value
      self.head = self.head.next_node
      return return_value
    return None
    
  def contains(self, value):
    currentNode = self.head
    while currentNode != None:
      if currentNode.value == value:
        return True
      currentNode = currentNode.next_node
    return False

  def get_max(self):
    if self.head == None:
      return None
    maxNode = self.head.value
    currNode = self.head
    while currNode is not None:
      if currNode.value > maxNode:
        maxNode = currNode.value
      currNode = currNode.next_node
    return maxNode

