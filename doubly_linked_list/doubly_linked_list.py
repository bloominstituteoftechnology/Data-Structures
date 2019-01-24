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
    # create a new node to add
    new_node = ListNode(value)
    # point the new nodes next val to existing head node
    new_node.next = self.head
    # make the head node the newly created node
    self.head = new_node
    # incase head is empty just make the tail as the new node as well
    if self.head is None:
      self.tail = new_node
      

  def remove_from_head(self):
    # if list is empty:
    if not self.head:
      return None
    # if only 1 element in list
    if self.head.next is None:
      old = self.head
      self.head = None 
      self.tail = None
      return old.value
     
    oldVal = self.head.value
    next = self.head.next
    self.head = next
    return oldVal

  def add_to_tail(self, value):
    # create node
    new_node = ListNode(value)
    # if list empty
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else: 
      self.tail.next = new_node
      self.tail = new_node

  def remove_from_tail(self):
    if not self.tail:
      return None
    prev_node = self.tail.prev
    self.tail = prev_node
    self.tail.next = None

  def move_to_front(self, node):
    if node.prev is not None:
      node.prev.next = node.next
    
    if node.next is not None:
      node.next.prev = node.prev

    self.head.prev = node
    node.prev = None
    node.next = self.head
    self.head = node

  def delete(self, node):
    node.delete()

  def move_to_end(self, node):
    if node.prev is not None:
      node.prev.next = node.next
    
    if node.next is not None:
      node.next.prev = node.prev

    self.tail.next = node
    node.prev = self.tail
    node.next = None
    self.tail = node

    
  def get_max(self):
    # if list is empty
    if not self.head:
      return None

    currentNode = self.head
    largest = self.head.value
    while currentNode is not None:
      if currentNode.value > largest:
        largest = currentNode.value
        currentNode = currentNode.next
      else:
        currentNode = currentNode.next
    return largest
