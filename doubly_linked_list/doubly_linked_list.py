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
      current_next.prev = self.next # This is a comment. asdasd

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
    # Use node or self to target insert before fn and feed it a value.
    node = ListNode(value)
    # node.delete()
    # self.head = value
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      self.head.insert_before(value)
      # node.next = self.head
      # self.head.prev = node
      self.head = self.head.prev

    self.length += 1

  def remove_from_head(self):
    temp = self.head
    del self.head
    return temp

  def add_to_tail(self, value):
    node = ListNode(value)
    self.tail.insert_after(node)

  def remove_from_tail(self):
    temp = self.tail
    del self.tail
    return temp

  def move_to_front(self, node):
    temp = node
    node.delete()
    self.add_to_head(temp)

  def move_to_end(self, node):
    temp = node
    node.delete()
    self.add_to_tail(temp)

  def delete(self, node):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev
    
  def get_max(self):
    # while self.head == None:
    #   return None
    # while self.head != None:
    #   max_val = self.head.value
    #   temp_node = self.head
    #   if temp_node.next:
    #     temp_node = temp_node.next
    #   if temp_node.value > max_val:
    #     max_val = temp_node.value
    #
    #   return max_val
    if self.head == None:
      return None
    else:
      cur_max = self.head.value
      cur_node = self.head
      while cur_node.next:
        cur_node = cur_node.next
        if cur_node.value > cur_max:
          cur_max = cur_node.value
    return cur_max