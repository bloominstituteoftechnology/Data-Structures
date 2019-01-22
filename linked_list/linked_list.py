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
    if self.head == None:
      self.head = new_node
    if self.tail == None:
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node
    #return self.tail.value

  def remove_head(self):
    if self.head:
      tmp = self.head

      if self.head.next_node is not None:
        self.head = self.head.next_node
      else:
        self.head = None
        self.tail = None
      return tmp.value
      



  def contains(self, value):
    current_node = self.head
    if current_node == None:
      return False
    else:
      while current_node is not None:
        if current_node.value == value:
          return True
        current_node = current_node.next_node
      return False

  def get_max(self):
    if self.head:
      current_node = self.head
      max = 0
      while current_node is not None:
        if current_node.value  > max:
          max = current_node.value
        current_node = current_node.next_node
        
      return max



# list = LinkedList()
# list.add_to_tail(2)
# list.add_to_tail(200)
# list.add_to_tail(400)
# print(list.tail.value)
# print(list.contains(500))
