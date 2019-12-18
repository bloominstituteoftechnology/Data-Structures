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
    
    def __repr__(self):
      return f"data: {self.value}"


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
    new_node = ListNode(value, None, None)
    self.length += 1
    # If list is empty
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.insert_after(self.head)
      self.head = new_node

  def remove_from_head(self):
    value = self.head.value
    self.delete(self.head)
    return value

  def add_to_tail(self, value):
    new_node = ListNode(value, None, None)
    self.length += 1
    # If list is empty
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.insert_before(self.tail)
      self.tail = new_node

  def remove_from_tail(self):
    value = self.tail.value
    self.delete(self.tail)
    return value


  def move_to_front(self, node):
    if node is self.head:
      return
    value = node.value
    self.delete(node)
    self.add_to_head(value)


  def move_to_end(self, node):
    if node is self.tail:
      return
    value = node.value
    self.delete(node)
    self.add_to_tail(value)

  def delete(self, node):
    if not self.head and not self.tail:
      # This shouldn't actually occur ever
      return
    self.length -= 1
    if self.head == self.tail:
      self.head = None
      self.tail = None
    elif self.head is node:
      self.head = node.next
      node.delete()
    elif self.tail is node:
      self.tail = node.prev
      node.delete()
    else:
      node.delete()

  def get_max(self):
    current = self.head
    max_value = current.value
    while current is not None:          
      if current.value > max_value:
        max_value = current.value
      current = current.next
    return max_value

  def __repr__(self):
    return f"LinkedList's head: {self.head}, and tail: {self.tail}"
