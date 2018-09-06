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

# node4 = Node(798)
node3 = Node(757)
node2 = Node(364)
node1 = Node(133)
# # print(node2.value)
# # print(node2.next_node.value)

# print(Node.get_value(node2))
# print(Node.get_value(Node.get_next(node2)))

# node3.set_next(node4)

# print(Node.get_value(Node.get_next(node3)))

#At this point I've confirmed that instantiating a node works, and that all the Node methods work. 


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
    # pass 

  def remove_head(self):
    if self.head == None:
      print('There is no head to remove.')
    elif self.head:
      self.head = self.head.get_next()
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



list1 = LinkedList()
list1.add_to_tail(node1)
list1.add_to_tail(node2)

# print(list1.head.value, list1.tail.value)
# print(Node.get_value(list1.head.value))
# print(Node.get_value(list1.tail.value))
print(list1.head.value.value)
print(list1.tail.value.value)

list1.contains(364)



#To add an element to the head of a list, we create a new node, set its element
#to the new element, set its next link to refer to the current head, and then set 
#the list's head to point to the new node. 

