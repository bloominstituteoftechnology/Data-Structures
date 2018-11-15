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
    exists = self.head
    while(exists):
      exists = exists.next_node
    exists = value
    self.tail = value
    return True

  def remove_head(self):
    # if head exists go on
      # 
      if self.head:
        if self.head.get_value() == None:
          temp_head = self.head

          self.head = None
          self.tail = None

          return temp_head.get_value()
        else:

    # else return None

  def contains(self, value):
    curr_node = self.head
    while(curr_node):
      if curr_node.value == value:
        return True
      else:
        curr_node = curr_node.next_node

  def get_max(self):
    curr_node = self.head
    greatest = 0
    while(curr_node):
      if curr_node.value > greatest:
        greatest = curr_node.value
      curr_node = curr_node.next_node
    return greatest


listing = LinkedList()
node_1 = Node(1)
node_2 = Node(4)
node_3 = Node(9)
node_4 = Node(33)

listing.head = node_1
listing.head.next_node = node_2
node_2.next_node = node_3


print(listing.contains(9))
print(listing.get_max())
print(listing.add_to_tail(node_4))