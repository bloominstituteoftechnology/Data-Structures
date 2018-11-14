class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    # if next is none, set next to value and prev to self
    # else, set the value of next to current node's next
    # and prev to current node and set the next node's prev
    # to value and current node's next to value
    if self.next is None:
      self.next = value
      value.prev = self
    else:
      value.next = self.next
      value.prev = self
      self.next.prev = value
      self.next = value

  def insert_before(self, value):
    # if prev is none, set prev to value and next to self
    # else, set the value of prev to current node's prev
    # and next to current node and set the prev node's next
    # to value and current node's prev to value
    if self.prev is None:
      self.prev = value
      value.next = self
    else:
      value.prev = self.prev
      value.next = self
      self.prev.next = value
      self.prev = value

  def delete(self):
    # if next is not none, set next's prev to current nodes
    # prev
    if self.next is not None:
      self.next.prev = self.prev
    
    # if prev is not none, set prev's nodes next to current
    # nodes next
    if self.prev is not None:
      self.prev.next = self.next

    # set current next and prev nodes to none and return
    # current node's value
    self.next = None
    self.prev = None
    return self.value

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

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
