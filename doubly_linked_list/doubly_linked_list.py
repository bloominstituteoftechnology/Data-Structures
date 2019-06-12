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
    pass
    # if self.head is None:
    #   self.head = ListNode(value)
    #   self.tail = self.head
    #   self.length = 1
    # else:
    #   old_head = self.head
    #   self.head = ListNode(value, None, old_head)
    #   self.length += 1

  def remove_from_head(self):
    if self.head is not None:
      self.head = self.head.next

  def add_to_tail(self, value):
    new_node = ListNode(value)
    self.length += 1
    if not self.tail and not self.head :
      self.tail = new_node
      self.head = new_node
    # if self.tail is None:
    #   print(f'here')
    #   self.tail = ListNode(value)
    #   self.head = self.tail
    #   self.tail.prev = self.head
    #   self.head.next = self.tail
    #   self.length = 1
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
    #   old_tail = self.tail
    #   self.head = ListNode(value, old_tail, None)
    #   self.length += 1
   

  def remove_from_tail(self):
    if not self.head and not self.tail :
      return None
    
    self.length -= 1
    if self.head == self.tail :
      current_tail = self.tail
      self.head = None
      self.tail = None
      return current_tail.value

    current_tail = self.tail
    self.tail = self.tail.prev
    self.tail.next = None
    return current_tail
    
    # if self.tail is not None:
    #   self.tail = self.tail.prev

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass

# q = DoublyLinkedList()
# q.add_to_tail(1)
# print(f' tail {q.tail.value}')
# print(f' tail prev {q.tail.prev.value}')