class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    self.next = ListNode(value, self, self.next)
    return self.next

  def insert_before(self, value):
    self.prev = ListNode(value, self.prev, self)
    return self.prev

  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev
    return self.value


class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    new_node = ListNode(value, None, self.head)

    if not self.head:
      self.tail = new_node
    else:
      self.head.prev = new_node
    
    self.head = new_node
    
  def remove_from_head(self):
    if not self.head: return None

    next_node = self.head.next
    retval = self.head.delete()
    self.head = next_node
      
    return retval

  def add_to_tail(self, value):
    if not self.tail:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
    else:
      self.tail = self.tail.insert_after(value)


  def remove_from_tail(self):
    if not self.tail:
      return None
    else:
      prev_node = self.tail.prev
      if prev_node:
        prev_node.next = None
      return self.tail.delete()

  def move_to_front(self, node):
    self.add_to_head(node.value)
    return node.delete()

  def move_to_end(self, node):
    self.add_to_tail(node.value)
    return node.delete()

  def delete(self, node):
    return node.delete()
