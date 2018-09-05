class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    new_node = ListNode(value)
    new_node.next = self.next
    new_node.prev = self
    # update existing prev / next links
    if not self.next == None:
      self.next.prev = new_node
    self.next = new_node

  def insert_before(self, value):
    new_node = ListNode(value)
    new_node.next = self
    new_node.prev = self.prev
    # update existing links
    self.prev = new_node
    self.prev.next = new_node

  def delete(self):
    # self.prev    self   self.next
    # self.prev --> self.next
    self.prev.next = self.next
    # self.prev <-- self.next
    self.next.prev = self.prev

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    new_node = ListNode(value)
    # if head does not exist (DNE)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    # else head DOES exist (+1 node)
    else:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node

  def remove_from_head(self):
    val = self.head.value
    # does list only contain one thing
    if self.head == self.tail:
      self.head = None
      self.tail = None
    # our list has two or more things
    else:
      new_head = self.head.next
      new_head.prev = None
      self.head = new_head
    return val

  def add_to_tail(self, value):
    new_node = ListNode(value)
    # if head does not exist (DNE)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node

  def remove_from_tail(self):
    val = self.tail.value
    if self.head == self.tail:
      self.head = None
      self.tail = None
    else:
      new_tail = self.tail.prev
      new_tail.next = None
      self.tail = new_tail
    return val

  def move_to_front(self, node):
    self.delete(node)
    self.add_to_head(node.value)

  def move_to_end(self, node):
    self.delete(node)
    self.add_to_tail(node.value)

  def delete(self, node):
    if node == self.head:
      self.remove_from_head()
    elif node == self.tail:
      self.remove_from_tail()
    else:
      node.delete()
