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
      self.head = ListNode(value)
      self.tail = self.head
    self.length += 1
  
  def remove_from_head(self): # need to return removed value
    old_head = self.head
    self.head.delete()
    if self.head.next:
      self.head = self.head.next
      self.head.prev = None
    else:
      self.head = None
      self.tail = None
    self.length -= 1
    return old_head.value

  def add_to_tail(self, value):
    if self.tail:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    else:
      self.tail = ListNode(value)
      self.head = self.tail
    self.length += 1

  def remove_from_tail(self):
    old_tail = self.tail
    if self.tail == self.head:
      self.tail = None
      self.head = None

    elif self.tail.prev:
      self.tail = self.tail.prev
      self.tail.next = None
      self.tail.delete()
    self.length -= 1
    return old_tail.value

    

  def move_to_front(self, node): # need to return value moved
    current_head = self.head # old head
    if self.head is not node:
      if node.next and node.prev: # if node has next and prev
        node.delete() 
      self.head = node # node becomes new head
      node.next = current_head
      self.head = node

  def move_to_end(self, node):
    if node == self.head:
      self.head = node.next
    self.delete(node)
    self.add_to_tail(node.value)

  def delete(self, node):
    node.delete()
    if node == self.head:
      if node.next:
        self.head = node.next
        self.head.prev = None
      else:
        self.head = None
    if node == self.tail:
      self.tail = None
    self.length -= 1
  
  def get_max(self):
    if not self.head:
      return None
    current_node = self.head
    list_max = 0
    while current_node:
      if current_node.value > list_max:
        list_max = current_node.value
      current_node = current_node.next
    return list_max

