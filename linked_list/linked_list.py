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
        self.tail.set_next(new_node)
        # takes the current node 1 and points to new node
        self.tail = new_node
        # assigns the new node 
        self.tail.set_next(None)
        print(self.tail.value)
      pass  


  def remove_head(self):
    print(self.head.value)
    nextt = self.head.get_next()
    print(nextt.value)
    print(self.head.value)
    print(self.tail.value)
    pass

  def contains(self, value):
    print("----------contains--------")
    print(self.head.value)

    if self.head.value == value:
      return True
    elif self.head.get_next() == value:
      return True 
    else: 
      x = self.head.get_next()
      while x != None: 
        print(x.value)
        if x.value == value:
          return True
        else: 
          x = x.get_next()
      # after a while 
      return False
    pass

  def get_max(self):
    pass

# notes
#  def add_to_tail(self, value):
#       print(self.tail, '-- self.tail A')
#       print(self.head, '-- self.head A')
#       new_node = Node(value)
#       print(new_node.get_value(), '-- new_node value')
#       if self.head == None:
#         print('no head', new_node)
#         self.head = new_node
#         print(self.head, '-- self.head B')
#         print(self.head.value, '-- self.head C')
#         self.tail = new_node
#         print(self.tail.value, '-- self.tail.value B')
#         print(self.head.get_next(), '41')
#       else:  
#         self.tail.set_next(new_node)
#         # takes the current node 1 and points to new node
#         self.tail = new_node
#         # assigns the new node 
#         self.tail.set_next(None)
#         print(self.tail.value, '-- self.tail B')
#         print(self.tail.get_next(), '-- self.tail next  B')
#         print(self.head.get_next().value, '46')
#         print(self.head.value, self.head.get_next(), self.head.get_next().get_next().value)
#       pass  
