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
      current_next.prev = self.next # This is a comment. asdasd

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

  def add_to_head(self, node):
    # Use node or self to target insert before fn and feed it a value.
    value = node
    # node.delete()
    # self.head = value
    self.head = value

  def remove_from_head(self):
    temp = self.head
    del self.head
    return temp

  def add_to_tail(self, value):
    self.tail = value

  def remove_from_tail(self):
    temp = self.tail
    del self.tail
    return temp

  def move_to_front(self, node):
    temp = node
    node.delete()
    self.add_to_head(temp)

  def move_to_end(self, node):
    temp = node
    node.delete()
    self.add_to_tail(temp)

  def delete(self, node):
    pass
    
  def get_max(self):
    temp = self.head
    if self.head.next > self.head:
      temp = self.head.next
