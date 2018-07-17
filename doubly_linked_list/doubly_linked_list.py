class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    node = ListNode(value, self)
    self.next = node

  def insert_before(self, value):
    node = ListNode(value, self.prev, self)
    self.prev = node

  def delete(self):
    if self.prev:
        self.prev.next = self.next
    if self.next:
        self.next.prev = self.prev

    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    self.head.insert_before(value)

  def remove_from_head(self):
    new_head = self.head.next
    self.head.delete()
    self.head = new_head

  def add_to_tail(self, value):
    self.tail.insert_after(value)

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
