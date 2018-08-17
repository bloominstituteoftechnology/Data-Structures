class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    new = ListNode(value, self.next, self)
    self.next = new
    return new

  def insert_before(self, value):
    new = ListNode(value, self.prev, self)
    self.prev = new
    return new

  def delete(self):
    if self.prev != None:
      self.prev.next = self.next
    if self.next != None:
      self.next.prev = self.prev
    return self

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    if self.head.next == None:
      self.head.next = self.tail
    self.head = self.head.insert_before(value)
    
  def remove_from_head(self):
    old_head = self.head
    if old_head != None:
      if old_head.next == None:
        self.tail = None
      old_head.delete()
    return old_head.value

  def add_to_tail(self, value):
    if self.tail.prev == None:
      self.tail.prev = self.head
    self.tail = self.tail.insert_after(value)

  def remove_from_tail(self):
    old_tail = self.tail
    if old_tail != None:
      if old_tail.prev == None:
        self.head = None
      old_tail.delete()
    return old_tail.value

  def move_to_front(self, node):
    current = self.head
    while current != None:
      if current == node:
        current.delete()
        self.add_to_head(node.value)
        break
      current = current.next

  def move_to_end(self, node):
    current = self.head
    while current != None:
      if current == node:
        current.delete()
        self.add_to_tail(node.value)
        break
      current = current.next

  def delete(self, node):
    node.delete()
