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
    #append
    #self.tail.next_node = Node(value)
    if self.head == None:
        self.head = Node(value)
    else:
        self.tail.set_next(Node(value))
        
    self.tail = Node(value)
    
  def remove_head(self):
    #if head exsits
    #remove it from linked list
    #change self.head to the next one "b"
    head = self.head 
    if self.head != None:
        self.head = self.head.get_next()
        return head.get_value()
    
  def contains(self, value):
    # get the input value and
    # check the input value with all the values of the linked list
    # return true if found 
    #else false
    #if self.head
    '''
    if self.head == None:
        return False
    if self.head.get_value() == value:
        return True
    else:
        self.head = self.head.get_next()
    ''' 
    container = self.head
    if container == None:
        return False
    if container.get_value() == value:
        return True
    
    while container != None:
        if container.get_value() == value:
            return True
        else:
            container = container.get_next()
        
    return False
    
    

  def get_max(self):
    pass
'''
nodeA = Node('a')
list = LinkedList()

list.add_to_tail(nodeA) # TypeError: add_to_tail() missing 1 required positional argument: 'value'

print(list.tail.value)

'''