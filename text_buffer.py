class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0
  def __len__(self):
    return self.length
  def add_to_head(self, value):
    new_node = ListNode(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
    self.length += 1
  def remove_from_head(self):
    prev_head = self.head
    if self.length == 0:
      return 
    else:
      new_head = self.head.next
      self.head.delete()
      self.head = new_head
      self.tail = self.tail if self.head is not None else None
      self.length -= 1
    return prev_head.value if prev_head is not None else prev_head
  def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head: 
            self.tail = new_node
            self.head = new_node
        else: 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
  def remove_from_tail(self):
    if not self.head and not self.tail:
      return None
    self.length -= 1
    if self.head == self.tail:
      current_tail = self.tail
      self.head = None
      self.tail = None
      return current_tail.value
    current_tail = self.tail
    self.tail = self.tail.prev
    self.tail.next = None
    return current_tail.value
  def move_to_front(self, node):
    if node is self.head:
      return
      value = node.value
    if node is self.tail:
      self.remove_from_tail()
    else:
      node.delete()
      self.length -= 1
      self.add_to_head(value)
  def move_to_end(self, node):
    if self.length > 1 and node != self.tail:
      current_node = node
      node.delete()
      self.tail.insert_after(current_node.value)
      self.tail = self.tail.next
      self.head = self.head if node != self.head else current_node.next
  def delete(self, node):
    self.length -= 1
    if not self.head and not self.tail:
      return
    if self.head == self.tail:
      self.head = None
      self.tail = None
    elif self.head == node:
      self.head = node.next
      node.delete()
    elif self.tail == node:
      self.tail = node.prev
      node.delete()
    else:
      node.delete()
  def get_max(self):
    if not self.head:
      return None
    max_val = self.head.value
    current = self.head
    while current:
      if current.value > max_val:
        max_val = current.value
      current = current.next
    return max_val
class TextBuffer: 
    def __init__(self, init=None):
        self.contents = DoublyLinkedList()
        if init:
            for char in init:
                self.contents.add_to_tail(char)
    def __str__(self):
        string = ""
        # needs to return a string to print 
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s
    def append(self, string_to_add):
        for char in string_to_add:
            self.contents.add_to_tail(char)
    def prepend(self, string_to_add):
        for char in string_to_add[::-1]:
            self.contents.add_to_head(char)
    def delete_front(self, chars_to_remove):
        for char in range(chars_to_remove):
            self.contents.remove_from_head()
    def delete_back(self, chars_to_remove):
        for char in range(chars_to_remove):
            self.contents.remove_from_tail()
    def join(self, other_buffer): 
        self.contents.tail.next = other_buffer.contents.head
        other_buffer.contents.head.prev = self.contents.tail
        other_buffer.contents.head = self.contents.head
        self.contents.tail = other_buffer.contents.tail
    def join_string(self, string_to_join):
        new_buffer = TextBuffer(string_to_join)
        self.join(new_buffer)    

text = TextBuffer("Cat")
print(text)
text.join_string("Dog")
print(text)
text.append(" is ")
text.join(TextBuffer("weird."))
print(text)
text.delete_back(6)
print(text)
text.prepend("Hey! ")
print(text)
text.delete_front(4)
print(text)	