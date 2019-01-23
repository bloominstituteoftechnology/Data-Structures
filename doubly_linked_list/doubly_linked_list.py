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

  def add_to_head(self, value):
    node = ListNode(value)
    node.next = self.head
    self.head = node
    if not self.head:
      self.tail = node

  def remove_from_head(self):
    if not self.head:
      return None
    else:
      old_head = self.head
      self.head.next.prev = None
      self.head = self.head.next
      return old_head.value

  def add_to_tail(self, value):
    node = ListNode(value)
    if not self.head:
      self.head = node
    elif not self.tail:
      self.head.next = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node

  def remove_from_tail(self):
    if not self.head:
      return None
    else:
      old_tail = self.tail
      # self.tail.prev.next = None
      self.tail = self.tail.prev
      return old_tail.value
      

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass
