"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  # O(1)
  def get_value(self):
    return self.value

  # O(1)
  def get_next(self):
    return self.next_node

  # O(1)
  def set_next(self, new_next):
    self.next_node = new_next  # O(1)

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.max = None

  # O(1)
  def add_to_tail(self, value):
    # Create new node
    node = Node(value)  # O(1)
    # If the ll is not empty
    if self.tail is not None:
      # Then set the tail's next to the new node
      self.tail.set_next(node)  # O(1)
      self.tail = node  # O(1)
      # Set max to node if higher than current value
      if self.max.value < node.value:
        self.max = node  # O(1)
    else:
      # If it is empty, set the new node to the head and tail
      self.head = node
      self.tail = node
      # And set it to max
      self.max = node

  # O(1)
  def remove_head(self):
    # Check if the head is None
    if self.head is not None:
      # set the head nodes next node value to a temp var
      old_head = self.head  # O(1)
      # delete the head node (not actually needed because python deallocates on its own if no more refrences)
      del(self.head)  # O(1) mostlikely
      # Then set head to that temp
      self.head = old_head.next_node  # O(1)

      # Makes sure tail is also None if new_head is None
      if self.head is None:
        self.tail = None  # O(1)
      
      return old_head.value

  # O(n)
  def contains(self, value):
    # Set the current node to the head
    curr_node = self.head
    
    while True:  # Loops through each node until it finds value or ll ends -- O(n)
      # 1. If the node is null, return False (exit case)
      if curr_node is None:
        return False  # O(1)
      elif curr_node.value == value:
        # 2. Else if the node's value matches the query value, return True
        return True  # O(1)
      else:
        # 3. Otherwise, set the current node to the next node and start again
        curr_node = curr_node.next_node  # O(1)

  # O(1)
  def get_max(self):
    return self.max.value if self.max is not None else None
