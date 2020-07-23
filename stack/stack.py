class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None
    # reference to the tail of the list
    self.tail = None

  def add_to_tail(self, value):
    # wrap the input value in a node
    new_node = Node(value, None)
    # check if there is no head (i.e., the list is empty)
    if not self.head:
      # if the list is initially empty, set both head and tail to the new node
      self.head = new_node
      self.tail = new_node
    # we have a non-empty list, add the new node to the tail
    else:
      # set the current tail's next reference to our new node
      self.tail.set_next(new_node)
      # set the list's tail reference to the new node
      self.tail = new_node

  def remove_head(self):
    # return None if there is no head (i.e. the list is empty)
    if not self.head:
      return None
    # if head has no next, then we have a single element in our list
    if not self.head.get_next():
      # get a reference to the head
      head = self.head
      # delete the list's head reference
      self.head = None
      # also make sure the tail reference doesn't refer to anything
      self.tail = None
      # return the value
      return head.get_value()
    # otherwise we have more than one element in our list
    value = self.head.get_value()
    # set the head reference to the current head's next node in the list
    self.head = self.head.get_next()
    return value

  def contains(self, value):
    if not self.head:
      return False
  
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False
def delete(self, node):
        # TODO: Catch errors if list is empty or node is not in list
        # For now assumine node is in list
        # Node is the only item in list
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # Node is head
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        # Node is tail
        # Node is between head and tail
        else:
            node.delete()
def remove_from_tail(self):
    value = self.tail.value
    delattr(self.tail)
    return value



"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        return self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_from_tail()