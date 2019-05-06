class Node:
  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node
    
  def __str__(self):
    return f'Node({self.data})'

  def get_data(self):
    return self.data
    
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
    if not self.head or not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = self.tail.get_next()

  def remove_from_head(self):
    if not self.head or not self.tail:
      return None
    
    if self.head == self.tail:
      value = self.head.get_data()
      self.head = None
      self.tail = None
      return value
    else:
      old_head = self.head
      self.head = self.head.get_next()
      return old_head.get_data()

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    item = self.storage.remove_from_head()
    self.size -= 1 if self.size > 0 else 0
    return item

  def len(self):
    return self.size