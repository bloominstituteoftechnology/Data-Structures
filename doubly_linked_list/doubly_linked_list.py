"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.head == None:
      self.head = ListNode(value)
      self.tail = self.head
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
      # node = ListNode(value)
      # node.next = self.head
      # self.head = node
    self.length += 1

  def remove_from_head(self):
    value = None
    if self.head == None:
      value = None
    elif self.head == self.tail:
      value = self.head.value
      self.head = None
      self.tail = None
      self.length -= 1
    else:
      value = self.head.value
      self.head = self.head.next
      self.length -= 1
    
    return value

    if self.head == None:
      return None
    else:
      value = self.head.value
      self.head = self.head.next
      self.length -= 1
      return value

  def add_to_tail(self, value):
    if self.tail == None:
      self.head = ListNode(value)
      self.tail = self.head
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    self.length += 1

  def remove_from_tail(self):
    value = None
    if self.tail == None:
      value = None
    elif self.head == self.tail:
      value = self.tail.value
      self.head = None
      self.tail = None
      self.length -= 1
    else:
      value = self.tail.value
      self.tail = self.tail.prev
      self.length -= 1
    
    return value

  def move_to_front(self, node):
    value = node.value
    self.delete(node)
    self.add_to_head(value)

  def move_to_end(self, node):
    value = node.value
    self.delete(node)
    self.add_to_tail(value)

  def delete(self, node):
    if self.head == node:
      self.head = node.next
    if self.tail == node:
      self.tail = node.prev
    node.delete()
    self.length -= 1
    
  def get_max(self):
    max = self.head.value
    node = self.head
    while node.next:
      node = node.next
      if node.value > max:
        max = node.value
    return max
