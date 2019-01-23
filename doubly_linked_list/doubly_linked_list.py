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
    oldHead = self.head
    newNode = ListNode(value)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:    
      oldHead.insert_before(value)
      self.head = oldHead.prev  
    
    pass

  def remove_from_head(self):
    if self.head is None:
      return None
    newHead = self.head.next
    value = self.head.value
    self.head.delete()
    self.head = newHead
    return value

    
    pass

  def add_to_tail(self, value):
    self.tail.insert_after(value)
    self.tail = self.tail.next
    pass

  def remove_from_tail(self):
    if self.head is None:
      return None
    newTail = self.tail.prev
    value = self.tail.value
    self.tail.delete()
    self.tail = newTail
    return value
    pass

  def move_to_front(self, node):
    while node.prev is not None:
      node.delete()
      node.prev.insert_before(node.value)
      node = node.prev.prev
    self.head = node
    pass

  def move_to_end(self, node):
    if self.head is None:
      return None
    while node.next is not None:
      node.delete()
      node.next.insert_after(node.value)
      node = node.next.next
    self.tail = node
    pass

  def delete(self, node):
    if node is self.head:
      self.head = node.next
    if node is self.tail:
      self.tail = node.prev
    node.delete()
      

    pass
    
  def get_max(self):
    node = self.head
    if self.head is None:
      return None

    value = node.value
    while node.next is not None:
      node= node.next
      if node.value > value:
        value = node.value
      
    
    return value