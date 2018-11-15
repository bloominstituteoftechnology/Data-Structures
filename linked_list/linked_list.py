"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def __str__(self):
    return f'Node Value: {self.value}'

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
    # Define the head and tail
    head_node = self.head
    tail_node = self.tail

    # create a new node
    new_node = Node(value)

    # check if head and tail are none,
    # if none, set head and tal to the new node
    # else, set next tail node to new node and
    # tail to new node
    if head_node is None:
      self.head = new_node
    if tail_node is None:
      self.tail = new_node
    else:
      tail_node.set_next(new_node)
      self.tail = new_node
    

  def remove_head(self):
    # Check if head is none, if so, return none
    if self.head is None:
      return None

    # set the head's current value
    value = self.head.get_value()

    # set the head to the next node
    self.head = self.head.get_next()

    # if head is none, set tail to none as well
    if self.head is None:
      self.tail = None

    # return the heads value
    return value


  def contains(self, value):
    # set current node to head
    cur_node = self.head

    # while current node exists,
    # compare the values and return true if they are equal
    while cur_node:
      if cur_node.get_value() is value:
        return True
      cur_node = cur_node.get_next()
    return False


  def get_max(self):
    # set the current node
    cur_node = self.head

    # check if the node exists, if not return none
    if cur_node is None:
      return None
    
    # set the max value to the default first node
    max_value = cur_node.get_value()

    # continue while current node exists
    while cur_node:

      # check if the next node exists, if not, return max val
      if cur_node.get_next() is None:
        return max_value
      
      # set next node and next node's value and compare
      next_node = cur_node.get_next()
      next_value = next_node.get_value()
      if max_value < next_value:
        max_value = next_value

      # set current node to the next node and repeat
      cur_node = cur_node.get_next()

    return max_value

    # The one below was my first approach, but I also decided
    # to take another approach as show above. 
    # This bottom approach looks cleaner
    # and uses the built in function max, the other
    # checks each value manually

    # values = []
    # cur_node = self.head

    # if cur_node is None:
    #   return None

    # while cur_node:
    #   values.append(cur_node.get_value())
    #   cur_node = cur_node.get_next()
    
    # max_val = max(values)
    # return max_val
