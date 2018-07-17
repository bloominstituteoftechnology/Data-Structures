class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    self.next = ListNode(value, self, self.next)

  def insert_before(self, value):
    self.prev = ListNode(value, None, self)

  def delete(self):
    self.prev.next = self.next
    self.next.prev = self.prev

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_head(self, value):
    if self.head is not None:
      self.head.insert_before(value)
      self.head = self.head.prev
    else:
      self.head = ListNode(value)

  def remove_from_head(self):
    if self.head:
      removeValue = self.head.value
      self.head = self.head.next
      return removeValue
    return None

  def add_to_tail(self, value):
    last = ListNode(value)
    if self.head == None:
      self.head = last
    else:
      self.tail.insert_after(value)
    
    self.tail = last

  def remove_from_tail(self):
    removeValue = self.tail.value
    self.tail.value = self.head.value
    self.tail.prev = self.head
    self.tail.next = None
    
    return removeValue

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
