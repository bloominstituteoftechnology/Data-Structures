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
    current_head = self.head
    # if list is empty
    if not current_head:
      self.head = ListNode(value)
    # else insert before old head 
    # and new head is node before old head
    else:
      current_head.insert_before(value)
      self.head = current_head.prev
      self.length += 1 # increase list lenght
  
  def remove_from_head(self): # need to return removed value
    # if list is empty
    if not self.head:
      return None
    # if list not empty
    else:
      head = self.head # save old head
      self.head.delete() # delete head
      self.length -= 1 # decrease list length
      return head.value # return old head (deleted)

  def add_to_tail(self, value):
    current_tail = self.tail
    # if list is empty
    if not self.head:
      return None
    # if list not empty
    else:
      current_tail.insert_after(value) # insert after old tail
      self.tail = current_tail.next # new tail is new node after old tail
      self.length += 1 # increase list length

  def remove_from_tail(self):
    # if list is empty
    if not self.head:
      return None
    # if list of 1 node
    if self.head == self.tail:
      # head and tail become None
      tail = self.tail
      self.head = None
      self.tail = None
      return tail.value
    else:
      tail = self.tail # old tail
      self.tail.delete() # delete old tail
      self.tail = tail.prev # new tail
      self.length -= 1 # decrease list length
      return tail.value # return old tail (deleted)

  def move_to_front(self, node): # need to return value moved
    if self.head is not node:
      if node.next and node.prev: # if node has next and prev
        node.delete() 
      current_head = self.head # old head
      self.head = node # node becomes new head
      node.next = current_head
      current_head.prev = node

  def move_to_end(self, node):
    if self.tail is not node:
      if node.next and node.prev:
        node.delete()
      current_tail = self.tail
      self.tail = node
      node.prev = current_tail
      current_tail.next = node

  def delete(self, node):
    if node.next is None and node.prev is not None:
      node.prev.next = None
      self.tail = node.prev
      return node.value
    if node.prev is None and node.next is not None:
      node.next.prev = None
      self.head = node.next
      return node.value
    if node.prev is None and node.next is None:
      self.head = None
      self.tail = None
      return node.value
    else:
      node.delete()
      if node == self.head:
        self.head = node.next
      if node == self.tail:
        self.tail = node.prev
    return node.value
  
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

