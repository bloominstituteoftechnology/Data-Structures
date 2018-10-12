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
    #create a node
    node=Node(value)

    #check if head is empty, means empty linked list, hence head and tail will be same

    if self.head==None:
        self.head=node
        self.tail=node
    else:
        self.tail.next_node = node
        self.tail=node

  def remove_head(self):
    if self.head==None:
        return None
    else:
        headvalue=self.head
        self.head=headvalue.get_next()
        if headvalue == self.tail:
            self.tail = None

        return headvalue.value

  def contains(self, value):
    element = self.head
    while element != None:
      if element.value == value:
        return True
      else:
        element = element.next_node
    return False

  def get_max(self):
    current = self.head

    if current == None:
      return None
    
    value=self.head.value
    while current:
      if value < current.value:
        value=current.value        
        current = current.next_node    
      else:
        current = current.next_node   
    return value
