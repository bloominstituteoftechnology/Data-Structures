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
    # create the node
    node = Node(value)
    # if tail != none | set next to node
    # if tail is none | set head as node
    if self.tail is not None:
      self.tail.set_next(node)
    else:
      self.head = node
    # set the tail as node
    self.tail = node 
    pass

  def remove_head(self):
    # if head != none
    if self.head is not None:
      removed = self.head.get_value()
      # get the next node from the head save to a temp variable
      temp_next = self.head.get_next()
      # set the temp variable to the head
      self.head = temp_next
      print(removed)
      if self.head is None:
        del(self.tail)
        self.tail = None
      return removed
    pass

  def contains(self, value):
    current = self.head
    # while tail is true
    while True:
      if current is None:
        return False
      elif current.value == value:
        return True
      # check if value matches node
      else:
        current = current.next_node
    # go to the next node
    pass

  def get_max(self):
    if self.tail == None:
      return None
    else:
      result = self.tail.value
    current = self.head
    while current != None:
      if current.value > result:
        result = current.value
        current = current.next_node
      else:
        current = current.next_node
    return result
    # set a results variable
    # while tail is true
    # if value is > results | result = value


ll = LinkedList()
ll.add_to_tail(4)
print(f'this should be 4:   {ll.head.value}')
print(f'this should be 4:   {ll.tail.value}')
ll.add_to_tail(7)
print(f'this should be 4:   {ll.head.value}')
print(f'this should be 7:   {ll.tail.value}')
ll.add_to_tail(9)
ll.remove_head()
print(f'this should be 7:   {ll.head.value}')
print(f'this should be 9:   {ll.tail.value}')
print(f'this should be False:   {ll.contains(1)}')
print(f'this should be 9:   {ll.get_max()}')
ll.add_to_tail(1)
ll.add_to_tail(5)
print(f'this should be 9:   {ll.get_max()}')
ll.add_to_tail(22)
print(f'this should be 22:  {ll.get_max()}')
ll.add_to_tail(15)
print(f'this should be 22:  {ll.get_max()}')
print(f'this should be 7:   {ll.head.value}')
ll.remove_head()
print(f'this should be 9:   {ll.head.value}')

