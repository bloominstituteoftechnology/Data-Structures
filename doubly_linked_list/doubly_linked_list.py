class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    newnode = ListNode(value, self, self.next)
    oldNext = self.next
    self.next = newnode
    if oldNext:
        oldNext.prev = newnode

  def insert_before(self, value):
    newnode = ListNode(value, self.prev, self)
    oldprev = self.prev
    self.prev = newnode
    if oldprev:
        oldprev.next = newnode

  def delete(self):
    prev = self.prev
    next = self.next
    if next:
        next.prev = prev
    if prev:
        prev.next = next
    return self.value

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    node = ListNode(value, None, self.head)
    self.head = node

  def remove_from_head(self):
    next = self.head
    self.head = next.next
    return next.delete()

  def add_to_tail(self, value):
    newnode = ListNode(value, self.tail, None)
    self.tail.next = newnode
    self.tail = newnode

  def remove_from_tail(self):
    prev = self.tail
    self.tail = prev.prev
    return prev.delete()

  def move_to_front(self, node):
    node.delete()
    node.prev = None
    node.next = self.head
    self.head = node

  def move_to_end(self, node):
    node.delete()
    node.prev = self.tail
    node.next = None
    self.tail = node

  def delete(self, node):
    pass
