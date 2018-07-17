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
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node 
      self.tail = new_node

  def remove_head(self):
    if self.head == None:
      return None

    # if the head is none this line will not run 
    curr_head = self.head
    if curr_head.next_node == None:
      self.head = None
      self.tail = None
    else: 
      self.head = curr_head.next_node
    return curr_head.value
   

  def contains(self, target):
      current = self.head

      while current is not None:
          if current.value == target:
              return True
          current = current.next_node
      return False
      
     
  def get_max(self):
    current = self.head
    if current == None:
      return None
    current_max = current.get_value()
   
    while current.get_next() is not None:
      current = current.get_next()
      current_val = current.get_value()
      if current_max < current_val:
        current_max = current_val
        return current_max
    return current_max


# lis = LinkedList()
# lis.add_to_tail(2)
# lis.add_to_tail(5)
# lis.add_to_tail(10)
# lis.add_to_tail(51)
# lis.add_to_tail(110)
# print(lis.contains(1))
# curr = lis.head 
#print(curr.get_next().value)
# while(curr.get_value() is not None):
#   print("found -", curr.get_value())
#   curr = curr.set_next(curr.next_node)
# print("finally frre")