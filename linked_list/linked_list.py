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
    # And set it to max
    self.max = None

  def add_to_tail(self, value):
    node = Node(value)
    # If the ll is not empty
    if self.tail is not None:
      # Then set the tail's next to the new node
      self.tail.set_next(node)
      self.tail = node
      # Set max to node if higher than current value
      if self.max.value < node.value:
        self.max = node
    else:
      # If it is empty, set the new node to the head
      self.head = node
      self.tail = node
      # And set it to max
      self.max = node

  def remove_head(self):
    # Check if the head is None
    if self.head is not None:
      # set the head nodes next node value to a temp var
      prev_head = self.head
      # delete the head node (not actually needed because python deallocates on its own if no more refrences)
      del(self.head)
      # Then set head to that temp
      self.head = prev_head.next_node
      
      if self.head is None:
        self.tail = None

      return prev_head.value

  def contains(self, value):
    curr_node = self.head

    while True:
      # 1. If the node is null, return False (exit case)
      if curr_node is None:
        return False
      elif curr_node.value == value:
        # 2. Else if the node's value matches the query value, return True
        return True
      else:
        # 3. Otherwise, set the current node to the next node and start again
        curr_node = curr_node.next_node


  def get_max(self):
    current_node = self.head
    max_value = 0
    if current_node != None:
      while current_node != None:
        temp_value = current_node.get_value()
        if temp_value > max_value  :
          max_value = temp_value
        else:
          current_node = current_node.get_next()
      return max_value
