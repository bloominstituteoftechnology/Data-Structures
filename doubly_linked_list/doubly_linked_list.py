"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node that it points to."""
  
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node that it points to."""
  
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
    node = ListNode(value)

    if not self.head:
      self.head = node

      if not self.tail: 
        self.tail = node
    else:
      current_head = self.head
      self.head = node
      self.head.next = current_head
      current_head.prev = self.head

      if current_head == self.tail:
        self.tail = current_head
      elif not current_head.next:
        current_head.next = self.tail

    self.length += 1
  
  def add_to_tail(self, value):
    node = ListNode(value)

    if not self.tail:
      self.tail = node

      if not self.head:
        self.head = node
    else:
      current_tail = self.tail
      self.tail = node
      self.tail.prev = current_tail
      current_tail.next = self.tail

      if current_tail == self.head:
        self.head = current_tail
      elif not current_tail.prev:
        current_tail.prev = self.head
    
    self.length += 1
    
  def remove_from_head(self):
    if not self.head:
      return None
    else: 
      current_head = self.head
      self.length -= 1

      if self.head == self.tail:
        self.head = None
        self.tail = None
        return current_head.value
      elif self.head.next.value:
        self.head = self.head.next

        if self.head == self.tail:
          self.head.next = None
          self.tail.prev = None

        return current_head.value

  def remove_from_tail(self):
    if not self.tail:
      return None
    else:
      current_tail = self.tail
      self.length -= 1

      if self.tail == self.head:
        self.tail = None
        self.head = None
        return current_tail.value
      elif self.tail.prev.value:
        self.tail = self.tail.prev

        if self.tail == self.head:
          self.tail.prev = None
          self.head.next = None
        
        return current_tail.value

  def move_to_front(self, node): 
    if node == self.tail and node != self.head :
      self.tail = self.tail.prev
    elif node.prev and node.next:
      node.next.prev = node.prev
      node.prev.next = node.next
    else: 
      return
    
    current_head = self.head
    self.head = node
    self.head.next = current_head
    self.head.prev = None
    current_head.prev = self.head

  def move_to_end(self, node):
    if node == self.head and node != self.tail:
      self.head = self.head.next
    elif node.prev and node.next:
      node.next.prev = node.prev
      node.prev.next = node.next
    else:
      return
    
    current_tail = self.tail
    self.tail = node
    self.tail.prev = current_tail
    self.tail.next = None
    current_tail.next = self.tail

  def delete(self, node):
    if node == self.head:
      self.remove_from_head()
    elif node == self.tail:
      self.remove_from_tail()
    else:
      node.prev.next = node.next
      node.next.prev = node.prev
      self.length -= 1

  def get_max(self):
    current_node = self.head

    if current_node:
      current_max = None

      while current_node:
        if current_max == None or current_node.value > current_max:
          current_max = current_node.value
        
        current_node = current_node.next
      
      return current_max
    else:
      return None