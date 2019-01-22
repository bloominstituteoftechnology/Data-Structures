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
    # create a new note
    node = Node(value)
    # if the Linked List is not empty
    if self.tail is not None:
      # then set the tail's next to the new Node
      self.tail.set_next(node)
    else:
      # if it is empty set the new node to the head
      self.head = node
    # set the Linked List tail to the new node
    self.tail = node

  def remove_head(self):
    # check if head is not None
    if self.head is not None:
      # set the heads nodes next nodes value to a temp var
      new_head = self.head.next_node
      # delete the head node
      del(self.head)
      # then set head equal to the temp value
      self.head = new_head

  def contains(self, value):
    # set the current node to the head
    cur_node = self.head
    while True:
      # 1. if the node is null return False
      if cur_node is None:
        return False
      # elif the nodes value matches the query value, return True
      elif cur_node.value == value:
        return True
      # otherwise set the current node to the tail and start from step 1
      else:
        cur_node = cur_node.next_node

  def get_max(self):
    # get current head
    cur_head = self.head
    # create a var for max value
    max_value = None
    # while there is a current head that we haven't checked
    while cur_head:
      # if max_value still has intital value or
      # if cur_head is greater than our current max value
      if max_value is None or cur_head.get_value() > max_value:
        # set max_value to our current head
        max_value = cur_head.get_value()
        # afterwards change our current head to the next value to check if the next value is greater or if there is no next value the loop will end
      cur_head = cur_head.get_next()
    # return the max_value to user
    return max_value


