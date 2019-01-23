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
    
    # Create a new node
    # If the tail doesn't exists, meaning the list is empty, head and tail will be node  
    # Else, set the tail's next node to be the new node  
    
    new_node = Node(value)    # new_node = Node(value, None)
    
    if self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:  # tail exists
      self.tail.set_next(new_node)  # tell existing tail that next node is the new one
      self.tail = new_node # new tail
    
  def remove_head(self):
    
    # Check if the head exist
    # If yes, save it to a temperary head
    # Delete the head
    # Set the new head to be the temperary head's next node
    
    if self.head is None:
      return None
    
    old_head = self.head
    old_value = old_head.get_value()
    self.head = old_head.get_next()
    
    # After changing the head, if the head is now none, also set the tail to none because the list is now empty
    if self.head is None:
      self.tail = None
      
    del(old_head)
      
    return old_value  # test expects us to return the old head value
    
    # the old head is still there, but the head pointer is directed at the next node.
    # after the method finishes, python will clean up the old head (sometime in the future) since nothing is referencing it anymore
    # to get rid of the old head completely, we do something like: del(old_head)
    
              
  def contains(self, value):
    
    # Set the current node to the head
    # If the node is null, return false
    # Else, if the node's value mathces the query value, return true
    # Otherwise, set the current node to the tail and start from step 1
    
    current_node = self.head
    
    while True:
      if current_node is None:
        return False
      elif current_node.get_value() == value:
        return True
      else:
        current_node = current_node.get_next()

  def get_max(self):
    
    # Get the current node
    # If the current node doesn't exist, meaning the list is empty, return
    # If the next node doesn't exist, meaning the list has only 1 element, return the current node's value
    # Loop through the list, and compare the current node's value to the next node's value
    # If the next node's value is greater, then set the current node to be the next node
    # Return the current node's value
    
    current_max = 0
    current_node = self.head
    
    while current_node is not None:
      if current_node.get_value() > current_max:
        current_max = current_node.get_value()
        
      current_node = current_node.get_next()
    
    return current_max
      
#ll = LinkedList()
#ll.add_to_tail(5)
#print(ll.head.value)
#ll.tail
#print(ll.tail.value)
#ll.add_to_tail(6)
#print(ll.head.value)
#print(ll.tail.value)
#print(ll.head.next_node.value)
#ll.remove_head()
#print(ll.head.value)
#print(ll.tail.value)

