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
    if self.prev != None:
      self.prev.next = self.next
    if self.next != None:
      self.next.prev = self.prev

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    if self.head != None:
      self.head.insert_before(value)
      self.head = self.head.prev
    else:
      self.head = ListNode(value)

  def remove_from_head(self):
    if self.head != None:
        currentHead = self.head
        self.head = self.head.next
        if currentHead == self.tail:
          self.tail = None
        return currentHead.value
    else:
        return None

  def add_to_tail(self, value):
    if self.tail != None:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    else:
      self.tail = ListNode(value)

  def remove_from_tail(self):
    if self.tail != None:
        currentTail = self.tail
        self.tail = self.tail.prev
        if currentTail == self.head:
          self.head = None
        return currentTail.value
    else:
        return None

  def move_to_front(self, node): #1 -> 2 -> 3 -> 4 -> 5
    if self.tail == node:
      value = self.tail.value
      self.tail.delete()
      self.add_to_head(value)

  def move_to_end(self, node):
    if self.head == node:
      value = self.head.value
      self.head.delete()
      self.add_to_tail(value)

  def delete(self, node):
    pass
