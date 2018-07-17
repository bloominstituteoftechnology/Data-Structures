class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    self.next = ListNode(value, self, self.next)

  def insert_before(self, value):
    self.prev = ListNode(value, self.prev, self)

  def delete(self):
    self.prev.next = self.next
    self.next.prev = self.prev


class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_head(self, value):
    pass

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
