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
    #Create an object Node for provided value
    new_node = Node(value)
    #If ll is empty, assign new Node to both head and tail
    if not self.head:
        self.head = new_node
        self.tail = new_node
    #otherwise, assign new node to tail.next_node
    else:
        self.tail.next_node = new_node
        self.tail = new_node

  def remove_head(self):
    #If there is head node
    if self.head != None: 
        #save head into currentHead
        currentHead = self.head
        #Assign 2nd node to be new head
        self.head = currentHead.get_next()
        #If there is 1 item in the list, then remove_head will also remove tail
        if currentHead == self.tail:
          self.tail = None
        return currentHead.value
    else:
        return None

  def contains(self, value):
    #start searching from head
    current = self.head
    #loop through each node, if node's value = value, then return True.
    while current != None:
      if current.value == value:
        return True
      else:
        current = current.next_node
    return False

  def get_max(self):
    current = self.head
    values = []
    if current == None:
      return None
    while current:
      values.append(current.value)
      current = current.next_node
    return max(values)

