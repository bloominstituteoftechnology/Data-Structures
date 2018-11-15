class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    if not self.next:
      self.next = ListNode(value, self)
    else:
      curr_next = self.next
      new_node = ListNode(value, self, curr_next)
      self.next = new_node
      curr_next.prev = new_node

  def insert_before(self, value):
    if not self.prev:
      self.prev = ListNode(value, None, self)
    else:
      curr_prev = self.prev
      new_node = ListNode(value, curr_prev, self)
      self.prev = new_node
      curr_prev.next = new_node

  def delete(self):
    if not self.prev:
      self.next.prev = None
    elif not self.next:
      self.prev.next = None
    else:
      self.next.prev = self.prev
      self.prev.next = self.next

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    # if there is no head, there is no tail either
    if not self.head:
      self.head = ListNode(value)
      self.tail = ListNode(value)
    else:
      new_node = ListNode(value, None, self.head)
      self.head.prev = new_node
      self.head = new_node
    return new_node

  def remove_from_head(self):
    if self.head:
      removed_head = self.head
      if self.head == self.tail:
        self.head = None
        self.tail = None
      else:
        self.head.next.prev = None
      return removed_head.value
    else:
      return None

  def add_to_tail(self, value):
    # if there is no tail, there is no head either
    if not self.tail:
      self.head = ListNode(value)
      self.tail = ListNode(value)
    else:
      new_node = ListNode(value, self.tail)
      self.tail.next = new_node
      self.tail = new_node
    return new_node

  def remove_from_tail(self):
    if self.tail:
      removed_tail = self.tail
      if self.head == self.tail:
        self.head = None
        self.tail = None
      else:
        self.tail.prev.next = None
      return removed_tail.value
    return None

  def contains(self, value, current_node):
    if current_node:
      if current_node.value == value:
        return current_node
      return self.contains(value, current_node.next)
    return False

  def move_to_front(self, node):
    selected_node = self.contains(node.value, self.head)
    if selected_node:
      if selected_node != self.head:
        selected_node.prev.next = selected_node.next
        if selected_node != self.tail:
          selected_node.next.prev = selected_node.prev
        return self.add_to_head(selected_node.value)
      return selected_node
    return None

  def move_to_end(self, node):
    selected_node = self.contains(node.value, self.head)
    if selected_node:
      if selected_node != self.tail:
        selected_node.next.prev = selected_node.prev
        if selected_node != self.head:
          selected_node.prev.next = selected_node.next
        return self.add_to_tail(selected_node.value)
      return selected_node
    return None

  def delete(self, node):
    node.delete()
