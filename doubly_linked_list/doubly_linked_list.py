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
    if self.head:
      self.head.insert_before(value)
      self.head = self.head.prev
    else:
      headnode = ListNode(value)
      self.head = headnode
      self.tail = headnode
    self.length += 1

  def remove_from_head(self):
    savehead = self.head.value
    self.delete(self.head)
    return savehead

  def add_to_tail(self, value):
    if self.tail:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    else:
      tailnode = ListNode(value)
      self.tail = tailnode
      self.head = tailnode
    self.length += 1

  def remove_from_tail(self):
    savetail = self.tail.value
    self.delete(self.tail)
    return savetail

  def move_to_front(self, node):
    self.delete(node)
    self.add_to_head(node.value)

  def move_to_end(self, node):
    self.delete(node)
    self.add_to_tail(node.value)

  def delete(self, node):
    if node is self.head and node is self.tail:
      self.head = None
      self.tail = None
    elif node is self.head:
      self.head = node.next
    elif node is self.tail:
      self.tail = node.prev

    node.delete()
    self.length -= 1 if self.length > 0 else 0
    
  def get_max(self):
    if not self.head or not self.tail:
      return None
    curnode = self.head
    maxval = curnode.value
    while curnode:
      maxval = curnode.value if curnode.value > maxval else maxval
      curnode = curnode.next
    return maxval
