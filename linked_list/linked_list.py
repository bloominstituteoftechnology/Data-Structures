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

  def display_values(self):
    current_node = self.head
    values = []
    while current_node:
      values.append(current_node.value)
      current_node = current_node.next_node
    return values

  def add_to_tail(self, value):
    new_node = Node(value)
    if not self.head and not self.tail:
        self.head = new_node
        self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node
      
  def remove_head(self):
    node_to_delete = self.head
    if not self.head:
        return None
    elif self.tail == self.head:
        self.tail = None
        self.head = None
        return node_to_delete
    else:
      node_to_delete.next = None
      self.head = self.head.next_node
    
      

  def contains(self, value):
    pass

  def get_max(self):
    pass

linked_list = LinkedList()
linked_list.add_to_tail(10)
linked_list.add_to_tail(20)

values = linked_list.display_values()
print(values)