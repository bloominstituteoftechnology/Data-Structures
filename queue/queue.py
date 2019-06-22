class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = def __init__(self, head=None, tail=None ):
      self.head = head
      self.tail = tail

  def enqueue(self, item):
    pass
    if head == None: 
      self.head = item
      self.tail = item
    else: 
      self.head = item

  def dequeue(self):
    pass

  def len(self):
    pass

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

  def set_value(self, value):
    self.value = value