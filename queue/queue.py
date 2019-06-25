class Queue:
	def __init__(self):
	  # what data structure should we
	  # use to store queue elements?
		self.storage = Linked_List()


	def enqueue(self, item):
		# if no value in the queue add head
		self.storage.enqueue(item)

	def dequeue(self):
		return self.storage.dequeue()

	def len(self):
		return self.storage.get_size()

	#que FIFO   <-- removing 1<-- adding
class Node:
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next_node = next_node
	
	def get_value(self):
		return self.value
	
	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next
	
	def set_value(self, new_value):
		self.value = new_value

class Linked_List:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def get_size(self):
		return self.size

	def dequeue(self, node=None):
		if self.head == None:
			return None
		elif self.head == self.tail:
			last_node = self.tail
			self.head = None
			self.tail = None
			self.size -= 1
			return last_node.get_value()
		else:
			temp = self.head
			self.head = self.head.get_next()
			self.size -= 1
			return temp.get_value()
			
			
	def enqueue(self, item):
		node = Node(item)
		if self.tail == None:
			self.tail = node
			self.head = node
		else:
			self.tail.set_next(node)  
			self.tail = node
		self.size += 1


items_queue = Queue()
print(items_queue.len())
items_queue.enqueue(1)
items_queue.enqueue(2)
print(items_queue.len())

