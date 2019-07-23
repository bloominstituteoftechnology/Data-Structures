class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.push(item)
  
  def dequeue(self):
    return self.storage.pop()

  def len(self):
    return self.storage.length

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def push(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
    elif not self.tail:
      self.head.next = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1

  def pop(self):
    if self.length == 0:
      return None
    popped = self.head.value
    self.head = self.head.next
    self.length -= 1
    return popped

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None