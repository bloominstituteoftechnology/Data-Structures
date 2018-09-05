class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    pass

  def insert_before(self, value):
    pass

  def delete(self):
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def __iter__(self):
    current_node = self.head
    while current_node:
      yield current_node
      current_node = current_node.next

  def add_to_head(self, value):
    new_node = ListNode(value)
    if not self.head:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def remove_from_head(self):
    if not self.head:
      return None
    else:
      old_head = self.head
      next_node = self.head.next
      next_node.prev = None
      self.head = next_node
      return old_head.value

  def add_to_tail(self, value):
    new_node = ListNode(value)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail = new_node

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass


# dll = DoublyLinkedList()
# dll.add_to_head(10)
# print(dll.head.value)
# dll.add_to_head(20)
