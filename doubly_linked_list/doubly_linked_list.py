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
    self.length+=1
    pass

  def remove_from_head(self):
    if self.length>1:
      head = self.head
      temp = self.head.next
      self.head.delete()
      self.head = temp
      self.length-=1
    elif self.length==1:
      head = self.head
      self.head=None
      self.tail=None
      self.length -= 1

    return head.value

  def add_to_tail(self, value):
    if self.tail:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    else:
      self.head = ListNode(value)
      self.tail = self.head
    self.length+=1
    pass

  def remove_from_tail(self):
    if self.length>1:
      tail = self.tail
      temp = self.tail.prev
      self.tail.delete()
      self.tail = temp
      self.length-=1
    elif self.length==1:
      tail = self.tail
      self.head=None
      self.tail=None
      self.length -= 1


    return tail.value

  def move_to_front(self, node):
    if self.length==1:
      pass
    if node is self.tail:
      self.tail = node.prev
    node.delete()
    self.length-=1
    self.add_to_head(node.value)
    pass

  def move_to_end(self, node):
    if self.length==1:
      pass
    if node is self.head:
      self.head=node.next

    node.delete()
    self.length -= 1
    self.add_to_tail(node.value)
    pass

  def delete(self, node):
    if node is self.head:
      self.head = node.next
    if node is self.tail:
      self.tail=node.prev
    node.delete()
    self.length-=1
    pass
    
  def get_max(self):
    max = 0
    if self.length:
      current = self.head
      max = current.value
    while current.next:
      if current.next.value > max :
        max = current.next.value
      current = current.next


    return max

