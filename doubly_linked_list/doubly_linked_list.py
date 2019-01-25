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

    if self.head is not None:
      self.head.insert_before(node)
    else:
      self.head = node

  def remove_from_head(self):

    self.head = self.head.next
    self.head.prev = None

  def add_to_tail(self, value):
    node = ListNode(value)

    if self.tail is not None:
      self.tail.insert_after(node)
    else:
      self.tail = node

  def remove_from_tail(self):
    self.tail = self.tail.prev
    self.tail.next = None

  def move_to_front(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      self.head.insert_before(node)


  def move_to_end(self, node):
    if self.tail is None:
      self.tail = node
      self.head = node
      return self.tail.value
    else:
      self.head.insert_after(node)
      return self.head.value

  def delete(self, node):
    if node.prev is None:
      self.head = node.next
    else:
      node.prev.next = node.next
    if node.next is None:
      self.tail = node.prev
    else: 
      node.next.prev = node.prev
    
  def get_max(self):
    pass
