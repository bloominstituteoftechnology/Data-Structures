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

  #first create new node
  def add_to_tail(self, value): #could also add value arg but dont need to.
    #create new node
    node = Node(value)
    #set tail of existing tail to next new node
    #cant set tail if none. if LL not empty set tail to new node. if empty set new node to head.
    if self.tail is not None:
        self.tail.set_next(node)
    else: 
        self.head = node
    #set LL tail to new node
    self.tail = node

  def remove_head(self):
      #check if head is none
      #set head node's next node value to a temp val
    if self.head is not None:
      #store value to be returned
      old_head = self.head.get_value()
      #assign new head
      new_head = self.head.next_node
      #if there is another item
      if new_head is not None:
        self.head = new_head
      else: 
        self.head = None
        self.tail = None
      return old_head
      
  def contains(self, value):
    #set current node to head. if node is null return false. 
    # elif node value matches query value return true. else set current node to tail.
    curr_node = self.head

    #while current node exists
    while curr_node:
      #if current node is equal to target value return true
      if curr_node.get_value() == value:
        return True
      #proceed to next node
      curr_node = curr_node.next_node
    #if value not in list
    return False

  def get_max(self):
    #if head is none return none
    if self.head is None:
      return None
    #set head as max value (temp val)  
    max_val = self.head.get_value()
    curr_node = self.head
    # step through each node and compare and if it's bigger set that as max.
    while curr_node is not None:
      if curr_node.get_value() > max_val:
        max_val = curr_node.get_value()
      curr_node = curr_node.get_next()
    #then return the value
    return max_val


# ll = LinkedList()
# ll.add_to_tail(5)
# #print(ll.head.value)
# ll.add_to_tail(10)
# ll.add_to_tail(3)
# print(ll.get_max())


