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
## ListNode Methods
# insert_after(value)
# insert_before(value)
# delete()
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    node = ListNode(value)

    if self.head != None and self.tail != None:
      self.head.insert_before(node)
      self.head = node

    else:
      self.head = node
      self.tail = node

  def remove_from_head(self):
    if self.head is None and self.tail is None:
      retval = None
    elif self.head == self.tail:
      retval = self.head.value
      self.head = None
      self.tail = None
    else:
      retval = self.head.value
      new_head = self.head.next
      self.head.delete()
      self.head = new_head
    return retval

  def add_to_tail(self, value):
    pass

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass

DLL = DoublyLinkedList()
DLL.add_to_head(5)
DLL.add_to_head(4)
print(DLL.remove_from_head())