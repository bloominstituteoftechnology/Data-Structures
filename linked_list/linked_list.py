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
    self.head = head
    self.tail = tail

  #first create new node
  def add_to_tail(self): #could also add value arg but dont need to.
    node = Node(value)
    #set tail of existing tail
    #cant set tail if none. if LL not empty set tail to new node. if empty set new node to head.
    if self.tail is not None:
        self.tail.set_next(node)
    else: 
        self.head = Node
    #set LL tail to new node
    self.tail = node

  def remove_head(self):
        #check if head is none
    if self.head is not None:
        new_head = self.head.next_node
        #setting head nodes to next with temp var
        
        #delete head node
        del(self.head)

        #then set head to that temp
        self.head = new_head

  def contains(self, value):
      #set current node to head. if node is null return false. 
      # elif node value matches query value return true. else set current node to tail.
      curr_node = self.head

      if curr_node is None: 
        return False
      elif curr_node.value == value:
        return True
      else: 
        curr_node = curr_node.next_node

  def get_max(self):
    curr_node = self.head
    max_node = self.head

    if curr_node.get_next().value > curr_node.max_node:
      max_node = curr_node.get_next()
      curr_node = curr_node.get_next()
    elif curr_node.get_next() is None:
      return max_node.value
    else curr_node == None: 
      raise ValueError("empty list")




