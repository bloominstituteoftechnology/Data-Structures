class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = Linked_List()

  def enqueue(self, item):
    if self.storage.head == None:
    			value = Node(item)
			self.storage.change_head(value)
			self.size =+ 1
		else:
			self.storage.change_tail(item)
			self.size += 1
  
  def dequeue(self):
    pass

  def len(self):
    pass
