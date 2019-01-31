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
    new_node = ListNode(value)
    new_node.next = self.head
    self.head = new_node

    if self.head is None:
      self.tail = new_node

    pass

  def remove_from_head(self):
    removed = self.head.value
    self.head.delete()
    return removed

    pass

  def add_to_tail(self, value):
    if self.tail is not None:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    pass

  def remove_from_tail(self):
    removed = self.tail.value
    self.tail.delete()
    return removed
    pass

  def move_to_front(self, node):
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
    self.head.prev = node
    node.prev = None
    node.next = self.head
    self.head = node
    pass

  def move_to_end(self, node):
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
    self.tail.next = node
    node.prev = self.tail
    node.next = None
    self.tail = node
    pass

  def delete(self, node):
    node.delete()
    pass
    
  def get_max(self):
    if self.head:
      current_node = self.head
      max = 0
      while current_node is not None:
        if current_node.value > max:
          max = current_node.value
        current_node = current_node.next
      return max
    pass
