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
    self.head.insert_before(value)
    oldHead = self.head
    newHead = self.head.prev
    self.head = newHead
    self.head.next = oldHead

  def remove_from_head(self):
    self.head.delete()
    return self.head.value

  def add_to_tail(self, value):
    self.tail.insert_after(value)
    oldTail = self.tail
    newTail = self.tail.next
    self.tail = newTail
    self.tail.prev = oldTail
    return self.tail.value

  def remove_from_tail(self):
    self.tail.delete()
    return self.tail.value

  def move_to_front(self, node):
    oldHead = self.head
    print(node.next)
    self.head = node 
    self.head.prev = oldHead.prev
    oldHead.next = node.next
    self.head.next = oldHead
    self.head.next.prev = self.head
  
  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass
