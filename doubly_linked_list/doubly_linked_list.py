class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    new_node = ListNode(value)
    next_node = self.next
    self.next = new_node
    new_node.prev = self

    if next_node is not None:
      next_node.prev = new_node
      new_node.next = next_node

  def insert_before(self, value):
    new_node = ListNode(value)
    prev_node = self.prev
    self.prev = new_node
    new_node.next = self

    if prev_node is not None:
      prev_node.next = new_node
      new_node.prev = prev_node

  def delete(self):
    if self.prev is not None:
      self.prev.next = self.next

    if self.next is not None:
      self.next.prev = self.prev

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    if self.head is None:
      self.head = self.tail = ListNode(value)
      return

    self.head.insert_before(value)
    self.head = self.head.prev

  def remove_from_head(self):
    if self.head is None:
      return None

    ret = self.head.value
    self.delete(self.head)
    return ret

  def add_to_tail(self, value):
    if self.tail is None:
      self.tail = self.head = ListNode(value)
      return

    self.tail.insert_after(value)
    self.tail = self.tail.next

  def remove_from_tail(self):
    if self.tail is None:
      return None

    ret = self.tail.value
    self.delete(self.tail)
    return ret

  def move_to_front(self, node):
    val = node.value
    self.delete(node)
    self.add_to_head(val)

  def move_to_end(self, node):
    val = node.value
    self.delete(node)
    self.add_to_tail(val)

  def delete(self, node):
    if self.head == node:
      self.head = self.head.next

    if self.tail == node:
      self.tail = self.tail.prev

    node.delete()