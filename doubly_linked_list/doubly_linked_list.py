class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    self.next = ListNode(value, self)

  def insert_before(self, value):
    self.prev = ListNode(value, None, self)

  def delete(self):
    if self.next != None:
      self.next.prev = self.prev
    if self.prev != None:
      self.prev.next = self.next

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    new_node = ListNode(value, None, self.head)
    self.head.prev = new_node
    self.head = new_node

  def remove_from_head(self):
    value = self.head.value
    self.head = self.head.next
    self.head.prev = None
    return value

  def add_to_tail(self, value):
    new_node = ListNode(value, self.tail)
    self.tail.next = new_node
    self.tail = new_node

  def remove_from_tail(self):
    value = self.tail.value
    self.tail = self.tail.prev
    self.tail.next = None
    return value

  def move_to_front(self, node):
    if node == None:
      return
    if(self.head == node):
      return
    if node.prev != None:
      node.prev.next = node.next
    if node.next != None:
      node.next.prev = node.prev
    self.add_to_head(node.value)
    if self.tail == node:
      self.tail = self.tail.prev

  def move_to_end(self, node):
    if node == None:
      return
    if(self.tail == node):
      return
    if node.prev != None:
      node.prev.next = node.next
    if node.next != None:
      node.next.prev = node.prev
    self.add_to_tail(node.value)
    if self.head == node:
      self.head = self.head.next

  def delete(self, node):
    if node == None:
      return
    if node.prev != None:
      node.prev.next = node.next
    if node.next != None:
      node.next.prev = node.prev
    if node == self.head:
      self.head = node.next
    if node == self.tail:
      self.tail = node.prev