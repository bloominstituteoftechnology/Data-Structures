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
    if self.next != None:
      self.next.prev = self.prev
    if self.prev != None:
      self.prev.next = self.next
    self.next = None
    self.prev = None
    return self.value

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
    if self.head != None:
      if self.head.next != None:
        self.head = self.head.next
        return self.head.prev.delete()
      else:
        value = self.head.value
        self.head = None
        self.tail = None
        return value
    return None
  def add_to_tail(self, value):
    self.tail.insert_after(value)
    if self.tail.prev == None:
      self.head = self.tail
    self.tail = self.tail.next
  def remove_from_tail(self):
    if self.tail != None:
      self.tail = self.tail.prev
      self.tail.next.delete()

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
