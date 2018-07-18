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
    #check to see if the list has a head. If not create both head and tail
    if self.head == None:
      self.head = new_node
      self.tail = new_node
      return
    #if the node exit, create the new old next to the existing last node
    self.tail.next_node = new_node
    #update the linked list tail reference
    self.tail = new_node


  def remove_head(self):

    '''
    # my version which is failed after the test got some update
    old_head = self.head
    if old_head != None:
      self.head = old_head.next_node
      return old_head.value
    return None
    '''

    #Sean's solution
    if not self.head:
      return None
    #if no next, then we have a single element
    if not self.head.next_node:
      #take a reference to the current head
      head = self.head
      #delete the list's head ref and also make sure the tail points to None
      self.head = None
      self.tail = None
      return head.value
    else:
      #if we have multiple elements in our list
      value = self.head.value
      self.head = self.head.next_node
      return value
      


  def contains(self, value):
    # my version    
    cur_head = self.head
    while cur_head != None:
      if cur_head.value == value:
        return True
      cur_head = cur_head.next_node
    return False

    '''
    #Sean's solution
    if not self.head:
      return None
    #assign the current node to a variable
    current = self.head
    #iterate through the list
    while current:
      if current.value == value:
        return True
      # move on to the next list node by updating current
      current = current.get_next()
    return False
    '''  

  def get_max(self):
    # my version
    if self.head == None:
      return None
    max_node = self.head.value
    cur_node = self.head
    while cur_node != None:
      if cur_node.value > max_node:
        max_node = cur_node.value
      cur_node = cur_node.next_node
    return max_node

    '''
    #Sean's solution
    if not self.head:
      return None
    max_value = self.head.value
    # set current to head's next
    current = self.head.get_next()
    while current:
      if current.value > max_value:
        #update max_value
        max_value = current.value
      current = current.next_node
    return max_value
    '''

    

