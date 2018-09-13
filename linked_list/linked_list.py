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


#ATTEMPT #2
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    newNode = Node(value)
    if self.head == None:
      self.head = newNode
      self.tail = newNode
    elif self.head:
      newNode.set_next(None)
      self.tail.set_next(newNode)
      self.tail = newNode

  def remove_head(self):
    if self.head == None:
      print('There is no head to remove.')
      self.tail = None
      return None
    elif self.head.get_next() == None:
      oldHead = self.head
      self.head = None
      self.tail = None
      return oldHead.value
    elif self.head:
      oldHead = self.head
      self.head = self.head.get_next()
      return oldHead.value

  def contains(self,value):
    currentNode = self.head
    foundNode = False
    while currentNode and foundNode is False:
      if currentNode.get_value() == value:
        foundNode = True
        print(f'Linked list contains value {value}')
        return True
      else:
        currentNode = currentNode.get_next()
    if currentNode == None:
      print(f'Linked list does not contain a value of {value}')
      return False
      
  def get_max(self):
      currentNode = self.head
      maximum = currentNode
      if currentNode == None:
        return None
      if currentNode.get_next() == None:
        maximum = currentNode.get_value()
      while currentNode.get_value() is not None:
        if currentNode.get_value() > maximum:
          maximum = currentNode.get_value()
        else:
          currentNode = currentNode.get_next()
      return maximum

# ######ATTEMPT 2 tests
# list1 = LinkedList()

# list1.add_to_tail(10)
# list1.add_to_tail(20)
# list1.add_to_tail(30)
# list1.add_to_tail(40)
# print(list1.remove_head())
# print(list1.get_max())


# print(list1.contains(20))
# print(list1.head.value)
# list1.remove_head()
# print(list1.head.value)









#To add an element to the head of a list, we create a new node, set its element
#to the new element, set its next link to refer to the current head, and then set 
#the list's head to point to the new node. 





# #ATTEMPT #1
# class LinkedList:
#   def __init__(self):
#     self.head = None
#     self.tail = None

#   def add_to_tail(self, value):
#     # newNode = Node(value)
#     newNode = value
#     if self.head == None:
#       self.head = newNode
#       self.tail = newNode
#     elif self.head:
#       newNode.set_next(None)
#       self.tail.set_next(newNode)
#       self.tail = newNode

#   def remove_head(self):
#     if self.head == None:
#       print('There is no head to remove.')
#     elif self.head:
#       self.head = self.head.get_next()
#     pass
  
#   def contains(self,value):
#     currentNode = self.head
#     foundNode = False
#     while currentNode and foundNode is False:
#       if currentNode.get_value() == value:
#         foundNode = True
#         return f'Linked list contains value {value}'
#       else:
#         currentNode = currentNode.get_next()
#     if currentNode == None:
#       return 'Value not in list.'

#   def get_max(self):
#     currentNode = self.head
#     while currentNode.get_next():
#       if currentNode.get_value() > currentNode.get_next().get_value():
#         maximum = currentNode.getValue()
#       else:
#         maximum = currentNode.get_next().get_value()
#         currentNode = currentNode.get_next()
#     return maximum
#
#
#
# node4 = Node(798)
# node3 = Node(757)
# node2 = Node(364)
# node1 = Node(133)
# # print(node2.value)
# # print(node2.next_node.value)

# print(Node.get_value(node2))
# print(Node.get_value(Node.get_next(node2)))

# node3.set_next(node4)
# print(Node.get_value(Node.get_next(node3)))