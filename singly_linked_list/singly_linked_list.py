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
    new_node = Node(value,None)
    # Check to see if List is empty
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node
  def add_to_head(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.set_next(self.head)
      self.head = new_node
  def remove_head(self):
    if not self.head:
      return None
      #Does the Head Have a Next or more then one Value
    if not self.head.get_next():
      head = self.head
      self.head = None
      self.tail = None
      return head.get_value()
    value = self.head.get_value()
    self.head = self.head.get_next()
    return value
  def contains(self,value):
    if not self.head:
      return False
    current = self.head
    while current:
      if current.get_value() == value:
        return True
      current = current.get_next()
    return False
  def get_max(self):
    if not self.head:
      return None
    current = self.head
    max_val = current.value
    while current:
      if current.value > max_val:
        max_val = current.value
      current = current.next_node
    return max_val