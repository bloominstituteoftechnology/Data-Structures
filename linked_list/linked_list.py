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
      #create new node with passed value
      node_to_add = Node(value)
      #check if head->next is pointing to Null , means empty linked list if yes head and tail will be same
      if self.head == None:
          self.head = node_to_add
          self.tail = node_to_add
      else:
          self.tail = node_to_add    

  def remove_head(self):
      #check if the linked-list is empty .. return None
      if self.head == None:
          return None
      else:
          head = self.head
          self.head = head.get_next()
          return head.value

  def contains(self, value):
      #check if the linked-list is empty .. return None
      if self.head == None:
          return None
      else:
          current = self.head
          while current.get_next() != None:
            if current.get_value() == value:
                return True
            else:
                current = current.get_next()
        
      return False

  def get_max(self):
      #check if the linked-list is empty .. return None
      if self.head == None:
          return None
      else:
          max = 0
          current = self.head
          while current != None:
            if current.get_value() > max:
                max = current.get_value()
            else:
                current = current.get_next()
        
      return max
