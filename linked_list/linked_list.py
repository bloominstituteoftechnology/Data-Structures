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

  def insert(self, value):
    new_node = Node(value)
    new_node.set_next(self.head)
    self.head = new_node

  def add_to_tail(self, value):
    node = Node(value)
    if self.tail is not None:
        self.tail.set_next(node)
    else:
        self.tail = node

  def remove_head(self):
    if self.head.next_node is not None:
      next = self.head.next_node
      self.head.set_next(next)
      return next

  def contains(self, value):
    currentNode = self.head
    while currentNode is not None:
      if currentNode.value == value:
        # print("yes")
        return True
      else:
        currentNode = currentNode.next_node
    return False
      

  def get_max(self):
    currentNode = self.head
    largest = self.head.value
    while currentNode is not None:
      if currentNode.value > largest:
        largest = currentNode.value
        currentNode = currentNode.next_node
      else:
        currentNode = currentNode.next_node
    return largest

# myList = LinkedList()
# myList.insert(10)
# myList.insert(2)
# myList.insert(66)
# myList.add_to_tail(1997)

# myList.contains(10)

