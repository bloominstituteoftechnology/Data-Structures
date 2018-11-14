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
    if self.head == None:
        new_tail = Node(value)
        self.head = new_tail
        self.tail = new_tail
    else:
        new_tail = Node(value)
        self.tail.set_next(new_tail)
        self.tail = new_tail

  def remove_head(self):
    if self.head == None:
        return
    elif self.head.next_node == None:
        head_to_return = self.head
        self.head = None
        self.tail = None
        #print(head_to_return.get_value())
        return head_to_return.get_value()
    else:
        next_head = self.head.next_node
        head_to_return = self.head
        self.head = next_head
        #print(head_to_return.get_value())
        return head_to_return.get_value()

  def contains(self, value):
    if self.head != None:
        presently_searching_node = self.head
    else:
        return
    while presently_searching_node.get_value() != self.tail.get_value():
        #print(presently_searching_node.get_value())
        if presently_searching_node.get_value() == value:
            return True
        else:
            presently_searching_node = presently_searching_node.get_next()
    if presently_searching_node.get_value() == value:
        return True
    else:
        return False

  def get_max(self):
    current_max = -9999999999
    if self.head != None:
        presently_searching_node = self.head
    else:
        return
    while presently_searching_node.get_value() != self.tail.get_value():
        if presently_searching_node.get_value() > current_max:
            current_max = presently_searching_node.get_value()
        else:
            presently_searching_node = presently_searching_node.get_next()
    if presently_searching_node.get_value() > current_max:
        current_max = presently_searching_node.get_value()
    return current_max
