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

  # def add_to_tail(self, value):
  #   current = self.head
  #   found = False
  #   while current and found is False:
  #     if Node.get_next(current) == None:
  #       found = True
  #       Node.set_next(current, value)
  #       return True
  #     else:
  #       current = Node.get_next(current)
  #     if current == None:
  #       print('error')
  #     return self.tail 

  def add_to_tail(self, value):
    current = self.head
    found = False
    while current and found is False:
      if Node.get_next(current) == None:
        found = True
        
        self.tail = current.set_next(value)
        # self.tail = current.set_next(value)
      else:
        current = Node.get_next(current)
    return self.tail
        # print(current.get_next().value)
        # print(self.head.value, self.tail.value)


  def remove_head(self):
    pass

  def contains(self, value):
    current = self.head
    found = False
    while current and found is False:
      if Node.get_value(current) == value:
        found = True
      else: 
        current = Node.get_next(current)
    if current== None:
      raise ValueError("Value not in list")
    return current

  def get_max(self):
    pass

node2 = Node(34)
node1 = Node(13, node2)
# # print(node1.get_next())
# # print(node1.value)


list1 = LinkedList()

# list1.add_to_tail(node2)
# print(list1.head.value)
# print(list1.tail.value)

#To add an element to the head of a list, we create a new node, set its element
#to the new element, set its next link to refer to the current head, and then set 
#the list's head to point to the new node. 

