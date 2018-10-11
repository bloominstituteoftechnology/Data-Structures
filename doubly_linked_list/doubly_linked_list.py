class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    node = ListNode(value)
    if self.next == None:
      self.next = node
      node.prev = self
    else:
      node.next = self.next
      node.prev = self
      self.next.prev = node
      self.next = node

  def insert_before(self, value):
    node = ListNode(value)
    if self.prev == None:
      self.prev = node
      node.next = self
    else:
      node.prev = self.prev
      node.next = self
      self.prev.next = node
      self.prev = node

  def delete(self):
    self.next.prev = self.prev
    self.prev.next = self.next
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    self.head.insert_before(value)
    if self.head.next == None:
      self.tail = self.head
    self.head = self.head.prev
  def remove_from_head(self):
    pass

  def add_to_tail(self, value):
    pass

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
