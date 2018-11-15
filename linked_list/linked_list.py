"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
#Creating a Linked List...https://www.tutorialspoint.com/python/python_linked_lists.htm
#"We create a Node object and create another class to use this node object. We pass the 
# appropriate values thorugh the node object to point the to the next data elements."
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
#we make methods to interact with the node class

#add_to_tail
#"This involves pointing the next pointer of the the current last node of the linked list
#to the new data node. So the current last node of the linked list becomes the second last 
# data node and the new node becomes the last node of the linked list."
  def add_to_tail(self, value):
    if self.head == None and self.tail == None:
      self.head = Node(value)
      self.tail = Node(value)
    else:
      if self.head.value == None and self.tail.value == None:
        self.head = Node(value)
        self.tail = Node(value)
      else:
        if self.head.next_node == None:
          self.head.set_next(value)
          self.tail = Node(value)

#similar to add_to_tail, but we are assigning a return value that will equal the head and then taking it off
#making the next value the new head
  def remove_head(self):
    if self.head == None and self.tail == None:
      return None

    if self.head.next_node != None:
      return_value = self.head.value
      self.head = Node(self.head.next_node)
      self.tail = Node(self.head.value)
      return return_value

#if the head, next value or tail contain the value we are looking for, then return true, it contians that value
  def contains(self, value):
    if self.head == None and self.tail == None:
      pass
    else:
      if self.head.value == value or self.head.next_node == value or self.tail.value == value:
        return True
      else:
        return False
#if the head value is grater than the tail, then return that, it will be the max value
  def get_max(self):
    if self.head == None:
      pass
    else:
      if self.head.value > self.tail.value:
        return self.head.value
      else:
        return self.tail.value
