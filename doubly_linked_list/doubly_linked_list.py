class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

# Insert the given value as this node's
#   `next` node
  def insert_after(self, value):
    newNode = ListNode(value)
    if self.next: self.next.prev = newNode
    newNode.next = self.next
    self.next = newNode

# Insert the given value as the this node's
#   `prev` node
  def insert_before(self, value):
    newNode = ListNode(value)
    if self.prev: self.prev.next = newNode
    newNode.prev = self.prev
    self.prev = newNode

# Delete this node (returns this node)
  def delete(self):
    if self.prev: self.prev.next = self.next
    if self.next: self.next.prev = self.prev
    return self.value

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

# Adds the given value as the new head
#   node of the list
  def add_to_head(self, value):
    if not self.head:
      newNode = ListNode(value)
      self.head = newNode
      self.tail = newNode
    else:
      newNode = ListNode(value, None, self.head)
      if not self.tail: self.tail = newNode
      self.head.insert_before(newNode)
      self.head = newNode

# Remove the list's current head. The list's
#   `head` pointer should point to the removed node's
#   `next` node
  def remove_from_head(self):
    if not self.head: return None
    retVal = self.head.value
    if not self.head.next:
      self.head = self.head.next
    else:
      self.head.delete()
      self.head = None
    return retVal

# Adds the given value as the new tail
#   node of the list
  def add_to_tail(self, value):
    if not self.tail:
      newNode = ListNode(value)
      self.tail = newNode
      self.head = newNode
    else:
      newNode = ListNode(value, self.tail, None)
      if not self.head: self.head = newNode
      self.tail.insert_after(newNode)
      self.tail = newNode

# Remove the list's current tail. The list's
#   `tail` pointer should point to the removed node's
#   `prev` node
  def remove_from_tail(self):
    if not self.tail: return None
    retVal = self.tail.value
    if self.tail.prev: self.tail = self.tail.prev
    else:
      self.tail.delete()
      self.tail = None
    return retVal

# Move the given node to the front of the
#   list. Update the list's `head` pointer
#   accordingly
  def move_to_front(self, node):
    if node == self.tail: self.remove_from_tail()
    if node == self.head: self.remove_from_head()
    node.delete()
    self.add_to_head(node.value)

  def move_to_end(self, node):
    if node == self.tail: self.remove_from_tail()
    if node == self.head: self.remove_from_head()
    node.delete()
    self.add_to_tail(node.value)

  def delete(self, node):
    node.delete()
