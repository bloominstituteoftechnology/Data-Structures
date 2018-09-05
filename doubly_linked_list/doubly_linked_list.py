class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    self.next = ListNode(value, self, self.next)

  def insert_before(self, value):
    self.prev = ListNode(value, self.prev, self)

  def delete(self):
    self.prev.next = self.next
    self.next.prev = self.prev
    
    # print(self.next.value)
      
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    if self.head is not None:
      self.head.insert_before(value)
      self.head = self.head.prev
    else:
      self.head = ListNode(value)

  def remove_from_head(self):
    if self.head:
      removeValue = self.head.value
      self.head = self.head.next
      return removeValue
    return None

  def add_to_tail(self, value):
    last = ListNode(value)
    if self.head == None:
      self.head = last
    else:
      self.tail.insert_after(value)
    
    self.tail = last

  def remove_from_tail(self):
    removeValue = self.tail.value
    self.tail.value = self.head.value
    self.tail.prev = self.head
    self.tail.next = None
    
    return removeValue

  def move_to_front(self, node):
    # keep the temporary head
    tempHead = self.head
    # 1. add node to the head (also reassign self.head)
    self.add_to_head(node.value)
    # in add_to_tail we did not set connection between the new and old tail
    self.head.next = tempHead
    
    # 2. remove the node
    self.remove_from_tail()
    
    # reassign self.tail
    if not node.prev.next:
      self.tail = self.tail.prev

  def move_to_end(self, node):
    # keep the temporary tail
    tempTail = self.tail
    # 1. add node to the end (also reassign self.tail)
    self.add_to_tail(node.value)
    # in add_to_tail we did not set connection between the new and old tail
    self.tail.prev = tempTail
    
    # 2. remove the node
    self.remove_from_head()
    
    # reassign self.head
    if not node.next.prev:
      self.head = self.head.next

  def delete(self, node):
    pass
