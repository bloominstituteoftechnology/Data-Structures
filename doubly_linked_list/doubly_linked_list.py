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
    #create new node
    new_dll = ListNode(value)
    #set tail of new_dll to head
    #set previous node to be null
    new_dll.next = self.head
    new_dll.prev = None
    if self.head is not None:
      self.head.prev = new_dll
    self.head = new_dll
  def remove_from_head(self):
    
    if self.head is not None:
      deleted_head = self.head
      del(self.head)
      self.head = deleted_head.next
    return deleted_head.value

  def add_to_tail(self, value):
    new_dll = ListNode(value)

    if self.tail is None:
      self.head = new_dll
      self.tail = new_dll
    else:
      new_dll.prev = self.tail
      self.tail = new_dll


  def remove_from_tail(self):
    if self.tail is not None:
      deleted_tail = self.tail
      del(self.tail)
      self.tail = deleted_tail.prev
    return deleted_tail.value

  def move_to_front(self, node):
  
    if node.prev:
      node.prev.next = node.next
    if node.next:
      node.next.prev = node.prev
    self.head.prev = node
    node.prev = None
    node.next = self.head
    self.head = node
  def move_to_end(self, node):

    if node.prev:
      node.prev.next = node.next
    node.next = None
    node.prev = self.tail
    self.tail = node

  def delete(self, node):
    node.delete()
    
  def get_max(self):
    pass
