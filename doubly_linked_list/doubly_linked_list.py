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
  def __init__(self):
    self.head = None
    self.tail = None

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
    new_head = self.head.next
    self.delete(self.head)
    self.head = new_head
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
    new_tail = self.tail.prev
    self.delete(self.tail)
    self.tail = new_tail
    return ret

  def move_to_front(self, node):
    cur = self.head
    while cur is not None:
      if cur.value == node.value:
        break
      cur = cur.next

    if cur is not None:
      self.delete(cur)
    self.add_to_head(node.value)

  def move_to_end(self, node):
    cur = self.head
    while cur is not None:
      if cur.value == node.value:
        break
      cur = cur.next

    if cur is not None:
      self.delete(cur)
    self.add_to_tail(node.value)

  def delete(self, node):
    node.delete()
    if self.head == node:
      self.head = self.head.next
    if self.tail == node:
      self.tail = self.tail.prev