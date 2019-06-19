
class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None

  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, node):
    self.next_node = node


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def add_to_tail(self, value):
    if self.tail == None:
      self.head = Node(value)
      self.tail = self.head
    else:
      self.tail.set_next_node(Node(value))
      self.tail = self.tail.get_next_node()

  def remove_from_head(self):
    if self.head == None:
      return None
    else:
      value = self.head.get_value()
      self.head = self.head.get_next_node()
      return value


class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    if self.size <= 0:
      return None
    self.size -= 1
    return self.storage.remove_from_head()

  def len(self):
    return self.size
