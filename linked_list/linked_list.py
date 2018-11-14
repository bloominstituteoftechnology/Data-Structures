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

    # define the prev node and
    # create a new node
    prev_node = None
    new_node = Node(value)

    # check if head and tail are none,
    # if none, set head and tal to the new node
    # else, set next tail node to new node and
    # tail to new node
    if head_node == None:
      self.head = new_node
    if tail_node == None:
      self.tail = new_node
    else:
      tail_node.set_next(new_node)
      self.tail = new_node
    

  def remove_head(self):
    pass

  def contains(self, value):
    # set current node to head
    cur_node = self.head

    # for returning if true or false
    does_contain = False

    # check if head contains the value
    if cur_node.value == value:
      does_contain = True

    # continue to loop if the node does have
    # a next node and check it's value
    while cur_node.next_node != None:
      cur_node = cur_node.next_node
      cur_value = cur_node.value
      if cur_value == value:
        does_contain = True
    
    return does_contain


  def get_max(self):
    pass


nlist = LinkedList()
nlist.add_to_tail(1)
nlist.add_to_tail(2)
nlist.add_to_tail(5)
nlist.add_to_tail(10)