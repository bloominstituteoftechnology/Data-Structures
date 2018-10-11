class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    new_node = ListNode(value)
    if self.next == None:
      self.next = new_node
      new_node.prev = self
    else:
      new_node.next = self.next
      new_node.prev = self
      self.next.prev = new_node
      self.next = new_node

  def insert_before(self, value):
    new_node = ListNode(value)
    if self.prev == None:
      self.prev = new_node
      new_node.next = self
    else:
      new_node.prev = self.prev
      new_node.next = self
      self.prev.next = new_node
      self.prev = new_node

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
    new_node = ListNode(value)
    if self.head == None:
      new_node = self.head
    else:
      self.head.prev = new_node
      new_node.next = self.head
      new_node.prev = None

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
