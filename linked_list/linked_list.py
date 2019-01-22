"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node  # pointer to the next, pointer is a memory address

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None  # first item
    self.tail = None  # last item

  def add_to_tail(self, value):
    # create a new node
    node = Node(value)  # node = Node(value, None)
    
    # If the Linked List is not empty
    if self.tail is not None:
      # Set the tail's next to the new node
      # current last node point to this node
      self.tail.set_next(node)
    else:
      # If is is empty, set the new node to the head
      self.head = node
    # Set the Linked List's tail to the new node
    self.tail = node
    

  def remove_head(self):
    # Check if the head is None
    if self.head is not None:
      # Set the head nodes next node value to a temp var
      new_head = self.head.next_node
      
      # Delete the head node
      del(self.head)
      
      # Set head to that temp
      self.head = new_head  # new_head might be none, if it is, we don't really care

  def contains(self, value):
    # Set the current node to the head
    current_node = self.head
    
    while True:
      # If the node is null, return false
      if current_node is None:
        return False
      elif current_node.value == value:
        # Else, if the node's value mathces the query value, return true
        return True
      else:
        # Otherwise, set the current node to the tail and start from step 1
        current_node = current_node.next_node

  def get_max(self):
    current_node = self.head
    
    # If Linked List is empty, return
    if current_node is None:
      return
    
    # If Linked List has only 1 element, return the element
    if current_node.next_node is None:
      return current_node.value
      
    # If there are more than 1 element, compare the current node to the next node.
    # Continue this loop as long as there is a next node.
    while True:
      if current_node.next_node is not None:
        if current_node.value < current_node.next_node.value:
          current_node = current_node.next_node
          
    return current_node.value
      
      
ll = LinkedList()
ll.add_to_tail(5)
print(ll.head.value)
ll.tail
print(ll.tail.value)
ll.add_to_tail(6)
print(ll.head.value)
print(ll.tail.value)
print(ll.head.next_node.value)
ll.remove_head()
print(ll.head.value)
print(ll.tail.value)

