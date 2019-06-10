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
    new_node = ListNode(value)
    old_head = self.head
    self.head = new_node
    self.head.next = old_head
    self.head.nex.prev = self
    
    pass

  def remove_from_head(self):
    self.head.next.prev = None
    self.head = self.head.next
    pass

  def add_to_tail(self, value):
    old_tail = self.tail
    old_tail.next = Node(value)
    self.tail = old_tail.next
    pass

  def remove_from_tail(self):
    old_tail = self.tail
    old_tail.prev.next = None
    self.tail = old_tail.prev
    pass

  def move_to_front(self, node):
    if node is not self.tail and node is not self.head:
        node.next.prev = node.prev
        node.prev.next = node.next
    
    elif node is self.tail:
        node.prev.next = None
        self.tail = node.prev
    
    elif node is self.head:
        return
    
    node.next = self.head
    node.prev = None
    self.head.prev = node
    self.head = node
    
    pass

  def move_to_end(self, node):
    if node is not self.tail and node is not self.head:
        node.next.prev = node.prev
        node.prev.next = node.next
    
    elif node is self.head:
        node.next.prev = None
        self.head = node.next
    
    elif node is self.tail:
        return
    
    node.prev = self.tail
    node.next = None
    self.tail.next = node
    self.tail = node
    pass

  def delete(self, node):
    node.prev = node.next.prev
    node.next = node.prev.next
    pass
    
  def get_max(self):
    if not self.head and not self.tail: return None
    
    current = self.head
    max_value = 0
    while current:
        if current.value > max_value:
            max_value = current.value
    current = current.next
    pass
