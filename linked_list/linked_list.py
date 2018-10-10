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
    #create a node
    node=Node(value)

    #check if head is empty, means empty linked list, hence head and tail will be same

    if self.head==None:
        self.head=node
        self.tail=node
    else:
        self.tail=node



  def remove_head(self):
    if self.head==None:
        return None
    else:
        head=self.head
        self.head=head.get_next()
        return head.value

  def contains(self, value):
    if self.head==None:
        return None
    else:
        element=self.head
        while element!=None:
            if element.value==value:
                return True
            else:
                element=element.get_next()
        
        return False

  def get_max(self):
    pass
