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
    if not isinstance(item, LinkedList):
      self = LinkedList(self)
    
    if self.head is None:
      self.head = item 
    else:
      self.tail.next = item

    self.tail = item 

    return

  def remove_head(self, value):
   current_value = 1
   current_node = self.head
   previous_node = None

   while current_node is not None:
     if current_value == value:
       if previous_node is not None: 
         previous_node.next = current_node.next
       else:
         self.head = current_node.next

         previous_node = current_node
         current_node = current_node.next
         current_value = current_value + 1
         return

  def contains(self):
    current = self.head
    count = 0 
    while count:
      count += 1
      current = current.get_next()
    return count

  def get_max(self, value):
    pass