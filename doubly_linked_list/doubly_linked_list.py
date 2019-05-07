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
    cur_head = self.head
    if not cur_head: 
      self.head = ListNode(value)
    else:
      cur_head.insert_before(value)
      self.head = cur_head.prev

  def remove_from_head(self):
    if not self.head:
      return None
    else:
      self.head.delete()
      return True
  def add_to_tail(self, value):
    cur_tail = self.tail
    if not self.head:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
    else:
      cur_tail.insert_after(value)
      self.tail = cur_tail.next

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    if self.head is not node:
      cur_head = self.head
      self.head = node
      node.next = cur_head
      cur_head.prev = node

  def move_to_end(self, node):
    pass

  def delete(self, node):
    node.delete()
    
  def get_max(self):
    pass
