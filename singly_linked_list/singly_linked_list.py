# linear data structure made up of nodes and refs to the next node

# lets make some node class
class Node:
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    """
    Method to get the value of a node
    """
    return self.value

  def get_next(self):
    """
    Method to get the next node
    """
    return self.next_node

  def set_next(self, new_next):
    """
    Method to update the node's "next_node"
    """
    self.next_node = new_next


# now lets think of how we can make nodes interact in a way that consolidates their pieces together

# lets make a LinkedList class
# think of the idea of having a head and a tail like a snake 
# where the snake can grow based upon having more links in it

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    # wrap the value in a new Node
    new_node = Node(value)

    # check if the linked list is empty
    if self.head == None and self.tail == None:
      # set the head and tail to the new node
      self.head = new_node
      self.tail = new_node
    # otherwise the list must have a head and tail
    else:
      # update the last node's "next_node" to the new node
      self.tail.set_next(new_node) # (Last node in chain).next_node = new_node
      # update the "self.tail" to point to the new node that we just added
      self.tail = new_node

  def remove_tail(self):
    """
    Remove the last node in the chain and return its value
    """
    # check for empty list
    if self.head == None and self.tail == None:
      # if true return None
      return None
    # check if there's only one node
    if self.head == self.tail:
      # store the value of the node that we are going to remove
      value = self.tail.get_value()
      # remove the node
      # setting the head and the tail to None
      self.head = None
      self.tail = None
      # return the stored value of the Node
      return value
    # otherwise
    else:
      # store the value of the node that we are going to remove
      value = self.tail.get_value()
      # we need to set the "self.tail" to the second to last Node
      # we can only do this by traversing the whole list from beginning to end

      # starting from the head
      current_node = self.head
      # keep iterating until the node after "current_node" is the tail
      while current_node.get_next() != self.tail:
        # keep looping
        current_node = current_node.get_next()

      # set the "self.tail" to the current_node
      self.tail = current_node

      # set the new tail's "next_node" to None
      self.tail.next_node = None

      # return Value
      return value

  def remove_head(self):
    # check for empty list
    if self.head == None and self.tail == None:
      # if true return None
      return None
    if self.head == self.tail:
      # store the value of the node that we are going to remove
      value = self.head.get_value()
      # remove the node
      # setting the head and the tail to None
      self.head = None
      self.tail = None
      # return the stored value of the Node
      return value
    else:
      # store the head's old value
      value = self.head.get_value()
      # set self.head to the old head's next
      self.head = self.head.get_next()
      # retun the value
      return value

