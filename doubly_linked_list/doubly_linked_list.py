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
    return self.value

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    self.head.insert_before(value)
    self.head = self.head.prev

  def remove_from_head(self):
    new_head = self.head.next
    removed_node = self.head.delete()
    self.head = new_head
    return removed_node

  def add_to_tail(self, value):
    self.tail.insert_after(value)
    self.tail = self.tail.next

  def remove_from_tail(self):
    new_tail = self.tail.prev
    removed_node = self.tail.delete()
    self.tail = new_tail
    return removed_node

  def move_to_front(self, node):
    if self.tail == node:
        self.tail = node.prev

    node.prev.next = node.next
    node.prev = None
    node.next = self.head
    self.head.prev = node
    self.head = node

  def move_to_end(self, node):
    if self.head == node:
        self.head = node.next
    
    node.next.prev = node.prev
    node.next = None
    node.prev = self.tail
    self.tail.next = node
    self.tail = node

  def delete(self, node):
    removed_node = node.delete()
    return removed_node
