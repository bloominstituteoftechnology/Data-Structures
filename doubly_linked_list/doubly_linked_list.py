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
    current_head = self.head
    if current_head == None:
      self.head = ListNode(value)
      self.tail = self.head
      self.length = 1
    else:
      current_head.insert_before(value)
      self.head = current_head.prev
      self.length += 1

  def remove_from_head(self):
    deleted = self.head.value
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      self.head = self.head.next
      self.head.prev.delete()
      self.length -= 1
    return deleted

  def add_to_tail(self, value):
    current_tail = self.tail
    if not current_tail:
      node = ListNode(value)
      self.head = node
      self.tail = node
      self.length = 1
    else:
      current_tail.insert_after(value)
      self.tail = current_tail.next
      self.length += 1

  def remove_from_tail(self):
    deleted = self.tail.value
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      self.tail = self.head.prev
      self.tail.next.delete()
      self.length -= 1
    return deleted

  def move_to_front(self, node):
    if self.head is not node:
      if node.next and node.prev:
        node.delete()

      current_head = self.head
      self.head = node
      node.next = current_head
      current_head.prev = node

  def move_to_end(self, node):
    if self.length > 1 and node != self.tail:
      self.tail.insert_after(node.value)
      self.tail = self.tail.next
    if node == self.head:
      self.head = node.next
    node.delete()

  def delete(self, node):
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length = 0
    elif self.head == node:
      self.remove_from_head()
    elif self.tail == node:
      self.remove_from_tail()
    else:
      node.delete()
      self.length -= 1
    
  def get_max(self):
    max = 0
    pointer = self.head
    while pointer:
      if pointer.value > max:
        max = pointer.value
      pointer = pointer.next
    return max