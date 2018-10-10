"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
    # Creates a node with a value in it, and references to the next node
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
      # Changes the node that this one references
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    #Creates a new node with a value that references none
    new_node = Node(value, None)
    # If there is no head, the new node becomes the head and tail
    if self.head == None:
        self.head = new_node
        self.tail = new_node
    # The current tail references the new node, then the new node becomes the tail
    else:
        self.tail.set_next(new_node)
        self.tail = new_node

  def remove_head(self):
      #Checks if the head is also the tail, if it is then remove both head and tail from linked list
      if self.head:
          if self.head.get_next() == None:
              head = self.head
              self.head = None
              self.tail = None
              return head.get_value()
           # Sets the head as the node after the current head
          else:
              value = self.head.get_value()
              self.head = self.head.get_next()
              return value
      else:
          return None

  def contains(self, value):
      # Starting with the head, go through each value and check if it matches
      current = self.head
      found = False
      while current and found is False:
          if current.get_value() == value:
              found = True
          else:
              current = current.get_next()
        # If it goes through list and current gets to none, return false
      if current is None:
        return False
      return current

  def get_max(self):
      # If there are no nodes then returns None
      if not self.head:
          return None
      # Starts with head value, and goes through each node comparing value. If max is smaller then value, value becomes max
      else:
          current = self.head
          max = None
          while current:
              if max is None or max < current.get_value():
                  max = current.get_value()
              current = current.get_next()
          return max
