class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    new_node=ListNode(value)
    new_node.prev=self
    new_node.next=self.next
    self.next=new_node

  def insert_before(self, value):
    new_node=ListNode(value)
    new_node.prev=self.prev
    new_node.next=self
    self.prev=new_node

  def delete(self):
    if self.prev is not None:
      self.prev.next=self.next
    if self.next is not None:
      self.next.prev=self.prev

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    self.head.insert_before(value)
    self.head=self.head.prev

  def remove_from_head(self):
    new_head=self.head.next
    decapitated_head=self.head
    self.delete(self.head)
    self.head=new_head
    return decapitated_head.value
    
  def add_to_tail(self, value):
    self.tail.insert_after(value)
    self.tail=self.tail.next

  def remove_from_tail(self):
    chopped_off_tail=self.tail
    self.tail=self.tail.prev
    self.delete(self.tail.next)
    return chopped_off_tail.value

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    node.delete()
