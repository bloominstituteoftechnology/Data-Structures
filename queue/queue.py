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
class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage=None
    self.current_head=None

  def enqueue(self, item):
    if self.storage is None:
      if self.current_head is None:
        self.current_head=ListNode(item)
      self.storage= self.current_head
      self.size+=1
    else:
      self.storage=self.storage.next
      self.size+=1
  
  def dequeue(self):
    if self.current_head==None:
      return None
    else:
      temp_head= self.current_head
      print(f"current head {self.current_head.value}")
      print(f"current head next {self.current_head.next}")
      self.current_head=self.current_head.next
      answer=temp_head.value
      temp_head.delete()
      self.size-=1
      return answer

  def len(self):
    return self.size
