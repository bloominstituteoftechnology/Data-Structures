class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = Linked_List()

  def enqueue(self, item):
    self.storage.add_tail(item)
    self.size += 1
  
  def dequeue(self):
    dequeued = None
    if self.storage.head != None:
      dequeued = self.storage.head.value
      self.storage.del_head()
      self.size -= 1
    return dequeued

  def len(self):
    return self.size

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
	
	def set_value(self, new_value):
		self.value = new_value

class Linked_List:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_head(self, value):
    new_head = Node(value, self.head)
    if self.head == None:
      self.tail = new_head
    self.head = new_head

  def del_head(self):
    if self.head.get_next() == None:
      self.tail = None
    self.head = self.head.get_next()

  def add_tail(self, value):
    if self.tail == None:
      self.add_head(value)
    else:
      new_tail = Node(value)
      self.tail.set_next(new_tail)
      self.tail = new_tail

  def del_tail(self):
    current = self.head
    if current.get_next() == None:
      self.head = None
      self.tail = None
    while current.get_next() == self.tail:
      current = current.get_next()
    self.tail = current
    self.tail.set_next(None)