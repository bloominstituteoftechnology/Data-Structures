class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    newnode = ListNode(value, self, self.next)
    oldNext = self.next
    self.next = value
    value.prev = self
    value.next = oldNext
    oldNext.prev = value

  def insert_before(self, value):
    oldprev = self.prev
    self.prev = value
    value.prev = oldprev
    value.next = this
    oldNext.next = value

  def delete(self):
    prev = self.prev
    next = self.next
    prev.next = next
    next.prev = prev

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    node = ListNode(value, None, self.head)
    self.head = node

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
