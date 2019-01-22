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
    # create a new node
    node = Node(value)
    # if the LL is not empty
    if self.tail is not None:
      #set the tails next to the new node
      self.tail.set_next(node)
    else:
      # if it is empty set the new node to the head
      self.head = node
    # set the LLs tail to the new node
    self.tail = node

  def remove_head(self):
    # check if the head is none, if it is
    if self.head is not None:
      return_val = self.head.value
    # set the head nodes next node to a temp var
      new_head = self.head.next_node
      # set the head to the temp variable
      self.head = new_head
    else:
      return_val = None

    return return_val

  def contains(self, value):
    # set the current node to the head
    curr_node = self.head
    while True:
      # 1 if the node is null return false
      if curr_node is None:
        return False
      # 2 else if the nodes value matches value, return true
      elif curr_node.value == value:
        return True
      # 3 otherwise, set the current node to the tail and start from step 1
      else:
        curr_node = curr_node.next_node

  def get_max(self):
    # set the currrent highest to the first
    current_highest = self.head
    # set current node to the first node
    current_node = self.head
    # while True to create a loop
    while True:
      # had to move None check higher
      # could not compare None.value
      if current_node.get_next() == None:
        return current_highest.value
      # check if the next node is higher and if so
      if current_node.get_next().value > current_highest.value:
        # set current_highest to current node
        current_highest = current_node.get_next()
        # set current node to next node
        current_node = current_node.get_next()
        
      #else
      else:
        # set current node to next node
        current_node = current_node.get_next()


#############
# TEST CODE #
#############

# LL = LinkedList()
# LL.add_to_tail(1)
# LL.add_to_tail(5)
# LL.add_to_tail(302)
# LL.add_to_tail(7)
# LL.add_to_tail(4)
# LL.add_to_tail(1)

# print(f'LL CONTAINS TRUE: {LL.contains(5)}')
# print(f'LL CONTAINS FALSE: {LL.contains(13)}')
# print(f'LL GET_MAX: {LL.get_max()}')