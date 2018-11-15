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

  def add_to_tail(self, node_value):

    if not isinstance(node_value, Node):
      node_value = Node(node_value)

    if self.head is None:
      self.head = node_value
    else:
      self.tail.set_next(node_value)
    
    self.tail = node_value
    # not sure what this return does
    return 

  def remove_head(self):
    if self.head:
      removed_head = self.head
      if self.head.next_node:
        self.head = removed_head.next_node
      else:
        self.head = None
        self.tail = None
    elif self.head is None:
      return None
    
    return removed_head.value

  def contains(self, value):
    current_node = self.head
    node_id = 1
    matches = []

    while current_node is not None:
      if current_node.value == value:
        matches.append(node_id)
      current_node = current_node.next_node
      node_id = node_id + 1

    if len(matches) == 0:
      return False
    else:
      return True
    
  def get_max(self):
    # print('*****************************')
    # print('tail node: ', self.tail.get_value())
    # print('head node: ', self.head.get_value())

    if not self.head:
      return None
    else:
      max_value = self.head.get_value()

      current_node = self.head

      while current_node:
        if current_node.get_value() > max_value:
          max_value = current_node.get_value()
          
        current_node = current_node.get_next()
        print('Current max: ', max_value)
      return max_value

test_linked_list = LinkedList()

test_linked_list.add_to_tail(100)
test_linked_list.add_to_tail(55)
test_linked_list.add_to_tail(101)
test_linked_list.get_max()

