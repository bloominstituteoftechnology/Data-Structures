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
    if self.head is None:
     node = ListNode(value)
     node.prev = None
     self.head = node
    else:
      node = ListNode(value)
      self.head.prev = node
      node.next = self.head
      self.head = node
      node.prev = None

  def remove_from_head(self):
    pass

  def add_to_tail(self, value):
    if self.head is None:
      node = ListNode(value)
      node.prev = None
      self.head = node
    else:
      node = ListNode(value)
      current = self.head
      while current.next:
        current = current.next
      current.next = node
      node.prev = current
      node.next = None
    
  
  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    # node.previous.next = node.next
    # node.previous = self.tail
    # node.next.previous = node
    # node.next = None
    # self.tail = node
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass

  def print_list(self):
    current = self.head
    while current:
      print(current.value)
      current = current.next

dllist = DoublyLinkedList()

dllist.add_to_head(0)
dllist.add_to_tail(1)
dllist.add_to_tail(3)
dllist.add_to_tail(4)
dllist.add_to_tail(5)
dllist.move_to_end(4)
dllist.print_list()