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
    if self.head is not None:
      self.head.insert_before(value)
      if self.head.next is None:
        self.head = self.tail
      self.head = self.head.prev
    else:
      self.head = ListNode(value)
      self.tail = ListNode(value)


  def remove_from_head(self):
    if self.head is None:
      return None
    else:
      removed = self.head.value
      self.head = self.head.next
      self.head.prev = None
      print(self.head.prev)
      return removed


  def add_to_tail(self, value):
    if self.tail is not None:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    if self.tail is None:
      self.tail = ListNode(value)


  def remove_from_tail(self):
    if self.tail is not None:
      removed = self.tail.value
      self.tail.prev.next = None
      self.tail = self.tail.prev
      return removed
    else:
      return None

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass
