class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    new_node = ListNode(value, self, self.next)
    self.next = new_node
    return self.next

  def insert_before(self, value):
    new_node = ListNode(value, self.prev, self)
    self.prev = new_node
    return self.prev

  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev
    self.prev = None
    self.next = None
    return self.value

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    self.head = self.head.insert_before(value)

  def remove_from_head(self):
    return self.head.delete()

  def add_to_tail(self, value):
    self.tail = self.tail.insert_after(value)

  def remove_from_tail(self):
    return self.tail.delete()

  def move_to_front(self, node):
    current_node = self.head
    while current_node != None:
      if current_node == node:
        self.add_to_head(node.value)
        current_node.delete()
        return node
      current_node = current_node.next
    
  def move_to_end(self, node):
    current_node = self.head
    while current_node != None:
      if current_node == node:
        self.add_to_tail(node.value)
        current_node.delete()
        return node
      current_node = current_node.next
  

  def delete(self, node):
    pass

