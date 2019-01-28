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
    # create a new node with the given value
    new_node = Node(value)
    # only time that the LL's tail will not have a value is when it is first initialized 
    # check that the LinkedList's tail has a value meaning LL is not empty
    if self.tail is not None:
      # set the LinkedList's tail's pointer to the new add value
      self.tail.set_next(new_node)
    # if it is empty set the new node to the head
    else:
      self.head = new_node
    # end the method with always setting the tail attribute value no matter what because thats what the method is for  
    self.tail = new_node

  def remove_head(self):
    # check if head exist
    if self.head:
      # check if there head has a next value 
      if self.head.get_next() == None:
        temp_value = self.head.value
        self.head = None
        self.tail = None
        return temp_value
      else:
        # head's next value does exist
        temp_value = self.head.value
        self.head = self.head.get_next()
        return temp_value
    else:
      return None

  def contains(self, value):
    pass

  def get_max(self):
    pass

