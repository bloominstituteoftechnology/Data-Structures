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
    self.head.insert_before(value)

  def remove_from_head(self):
    old_head = self.head
    if self.head.next:
        self.head = self.head.next
        self.head.prev = None
    self.head.delete()
    return old_head

  def add_to_tail(self, value):
      self.tail.insert_after(value)
  
  def remove_from_tail(self):
    old_tail = self.tail
    if self.tail.prev:
        self.tail = self.tail.prev
        self.tail.next = None
    self.tail.delete()
    return old_tail

  def move_to_front(self, node):
    node.delete()
    self.head.insert_before(node.value)

  def move_to_end(self, node):
    node.delete()
    self.tail.insert_after(node.value)
    pass

  def delete(self, node):
    node.delete()
    
  def get_max(self):
    current = self.head
    max_value = 0
    while current:
        if current.value > max_value:
            max_value = current.value
        current = current.next
    return max_value

